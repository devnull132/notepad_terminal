import keyboard 
from utils import Utils 
from commands import Commands

class TextEditor():
    def __init__(self, filename: str):
        self.buffer = []
        self.filename = filename 
        self.utils = Utils()
        self.commands = Commands()
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
                if keyboard.is_pressed("esc"):
                    for i in range(len(self.buffer)-1):
                        file.write(f"{self.buffer[i]}\n")
                    self.commands.handle_esc()
                txt = input(f"{num_line} ")
                num_line += 1
                self.buffer.append(txt)
                if txt == "all":
                    break 
            for i in range(len(self.buffer)-1):
                file.write(f"{self.buffer[i]}\n")
            else:
                self.buffer.clear()
