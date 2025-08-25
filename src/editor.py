from utils import Utils 

class TextEditor():
    def __init__(self, filename: str):
        self.buffer = []
        self.filename = filename 
        self.utils = Utils()
    def edit_text(self):
        ext = self.filename.split(".")[-1] 
        self.utils.design(extension=ext)
        num = 1
        while True:
            txt = input(f"{num} ")
            num += 1
            self.buffer.append(txt)

            
