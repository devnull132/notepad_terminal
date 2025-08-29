from editor import TextEditor

def main():
    filename = input("Введите имя файла: ")
    txt_editor = TextEditor(filename=filename)
    txt_editor.edit_text()

if __name__ == "__main__":
    main()

