import os


class Commands:
    
    def handle_backspace(self, line: str):
        return line[:-1]
    
    def handle_esc(self):
        os.system("cls" if os.name == "nt" else "clear")
        cmd = input("""Номер строки для перехода к ней\n
        'S' для сохранения\n
        'Q' для выхода\n
        'SQ' для выхода и сохранения""")
        return cmd

