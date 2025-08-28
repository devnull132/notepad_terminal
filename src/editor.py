from utils import Utils 

class TextEditor():
    def __init__(self, filename: str):
        self.buffer = []
        self.filename = filename 
        self.utils = Utils()
        self.is_save = False 
    def edit_text(self):
        ext = self.filename.split(".")[-1] 
        self.utils.design(extension=ext)
        num_line = 1
        with open(self.filename, "a+") as file:
            file.seek(0)
            content = file.readlines()
            for i in content:
                print(f"{num_line} {i}")
                num_line += 1
            while True:
                txt = input(f"\n{num_line} ")
                num_line += 1
                self.buffer.append(txt)
                if txt == "!=!quit!=!":
                    break
                elif txt == "!=!edit_line!=!":
                    self.utils.edit_line(buffer=content)
                elif txt == "!=!save":
                    self.is_save = True
            if self.is_save:
                for i in range(len(self.buffer)-1):
                    file.write(f"{self.buffer[i]}\n")
            self.buffer.clear()
