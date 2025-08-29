from utils import Utils 
import os 

class TextEditor():
    def __init__(self, filename: str):
        self.buffer = []
        self.filename = filename 
        self.utils = Utils()
        self.is_save = False 
        self.original_content = []
        
    def display_full_content(self):
        os.system("cls" if os.name == "nt" else "clear")
        self.utils.design(extension=self.filename.split(".")[-1])
        
        line_num = 1
        for line in self.original_content:
            print(f"{line_num:3} {line.rstrip()}")
            line_num += 1
        
        for line in self.buffer:
            if line not in ["!=!quit!=!", "!=!save!=!", "!=!edit_line!=!"]:
                print(f"{line_num:3} {line}")
                line_num += 1
        
        return line_num
    
    def get_full_content(self):
        full_content = []
        
        for line in self.original_content:
            full_content.append(line.rstrip())
        
        for line in self.buffer:
            if line not in ["!=!quit!=!", "!=!save!=!", "!=!edit_line!=!"]:
                full_content.append(line)
        
        return full_content
    
    def save_file(self):
        try:
            full_content = self.get_full_content()
            with open(self.filename, "w") as file:
                for line in full_content:
                    file.write(f"{line}\n")
            print(f"Файл '{self.filename}' успешно сохранен!")
            self.is_save = True
            
            self.original_content = [line + '\n' for line in full_content]
            self.buffer.clear()
            
            return True
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")
            return False
    
    def edit_text(self):
        try:
            with open(self.filename, "r") as file:
                self.original_content = file.readlines()
        except FileNotFoundError:
            self.original_content = []
            print(f"Создан новый файл: {self.filename}")
        
        current_line = self.display_full_content()
        
        while True:
            try:
                txt = input(f"{current_line:3} ")
                
                if txt == "!=!quit!=!":
                    if not self.is_save and (self.original_content or self.buffer):
                        choice = input("Есть несохраненные изменения. Сохранить перед выходом? (y/n): ")
                        if choice.lower() == 'y':
                            self.save_file()
                    print("Выход из редактора...")
                    break
                    
                elif txt == "!=!save!=!":
                    self.save_file()
                    current_line = self.display_full_content()
                    continue
                    
                elif txt == "!=!edit_line!=!":
                    full_content = self.get_full_content()
                    if full_content:
                        success = self.utils.edit(buffer=full_content)
                        if success:
                            self.original_content = [line + '\n' for line in full_content[:len(self.original_content)]]
                            self.buffer = full_content[len(self.original_content):]
                            current_line = self.display_full_content()
                        continue
                    else:
                        print("Файл пуст. Сначала добавьте строки.")
                        continue
                
                self.buffer.append(txt)
                current_line += 1
                
            except KeyboardInterrupt:
                print("\nПрервано пользователем. Для выхода введите '!=!quit!=!'")
                print("Для сохранения введите '!=!save!=!'")
                continue
            except EOFError:
                print("\nКонец ввода. Для выхода введите '!=!quit!=!'")
                continue
        
        if not self.is_save and (self.original_content or self.buffer):
            choice = input("Сохранить изменения перед выходом? (y/n): ")
            if choice.lower() == 'y':
                self.save_file()
        
        self.buffer.clear()
