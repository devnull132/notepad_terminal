import os
from colorama import  Fore, Style, init 

init(autoreset=True)

class Utils:
    def __init__(self):
        self.file_extensions = {
            "py": "Python",
            "java": "Java",
            "js": "JavaScript",
            "ts": "TypeScript",
            "cpp": "C++",
            "c": "C",
            "cs": "C#",
            "php": "PHP",
            "rb": "Ruby",
            "go": "Go",
            "rs": "Rust",
            "swift": "Swift",
            "kt": "Kotlin",
            
            "html": "HTML",
            "css": "CSS",
            "json": "JSON",
            "xml": "XML",
            "yml": "YAML",
            "yaml": "YAML",
            
            "sql": "SQL",
            "csv": "CSV",
            
            "md": "Markdown",
            "txt": "Text",
            "ini": "INI",
            "cfg": "Config",
            "conf": "Config",
            
            "sh": "Shell",
            "bat": "Batch",
            "ps1": "PowerShell",
            
            # Other
            "dockerfile": "Dockerfile",
            "gitignore": "Git Ignore"
        }
        
        self.color_scheme = {
            "programming": Fore.CYAN + Style.BRIGHT,
            "markup": Fore.GREEN + Style.BRIGHT,
            "data": Fore.YELLOW + Style.BRIGHT,
            "config": Fore.MAGENTA + Style.BRIGHT,
            "script": Fore.BLUE + Style.BRIGHT,
            "other": Fore.WHITE + Style.BRIGHT
        }

    def get_extension_type(self, extension: str) -> str:
        programming_exts = {"py", "java", "js", "ts", "cpp", "c", "cs", "php", "rb", "go", "rs", "swift", "kt"}
        markup_exts = {"html", "css", "md"}
        data_exts = {"json", "xml", "yml", "yaml", "sql", "csv"}
        config_exts = {"ini", "cfg", "conf", "gitignore"}
        script_exts = {"sh", "bat", "ps1"}
        
        if extension in programming_exts:
            return "programming"
        elif extension in markup_exts:
            return "markup"
        elif extension in data_exts:
            return "data"
        elif extension in config_exts:
            return "config"
        elif extension in script_exts:
            return "script"
        else:
            return "other"

    def check_extension(self, extension: str) -> str:
        return self.file_extensions.get(extension.lower(), extension)

    def print_ext(self, extension: str):
        terminal_width = os.get_terminal_size().columns
        
        extension_name = self.check_extension(extension)
        extension_type = self.get_extension_type(extension.lower())
        color = self.color_scheme.get(extension_type, self.color_scheme["other"])
        
        header = f"📁 {extension_name.upper()} 📁"
        
        centered_header = header.center(terminal_width)
        
        print(color + centered_header)
        
        print(Fore.YELLOW + "─" * terminal_width)

    def design(self, extension: str):
        os.system("cls" if os.name == "nt" else "clear")
        self.print_ext(extension)



