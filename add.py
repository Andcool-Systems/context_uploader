import winreg
import shutil
import os

def add_to_context_menu(program_path, menu_name, command):
    # Открываем ключ реестра для типов файлов
    key_path = r"\*\shell"
    key = winreg.OpenKey(winreg.HKEY_CLASSES_ROOT, key_path, 0, winreg.KEY_WRITE)
    
    # Создаем новый ключ для контекстного меню
    new_key_path = winreg.CreateKey(key, menu_name)
    winreg.CloseKey(new_key_path)

    icon = winreg.CreateKey(key, menu_name)
    winreg.SetValueEx(icon, "icon", 0, winreg.REG_SZ, program_path)
    winreg.CloseKey(icon)

    
    # Создаем подключ "command" и устанавливаем команду для запуска программы
    command_key_path = winreg.CreateKey(key, menu_name + r"\command")
    winreg.SetValueEx(command_key_path, "", 0, winreg.REG_SZ, command)
    winreg.CloseKey(command_key_path)
    
    # Закрываем открытый ключ
    winreg.CloseKey(key)


if __name__ == "__main__":
    main_path = r"C:\Program Files\fuUploader"
    if not os.path.exists(main_path):
        os.makedirs(main_path)
    
    shutil.copy2('uploader.exe', main_path + 'uploader.exe')
    program_path = main_path + "uploader.exe"
    menu_name = "Upload file to fu.andcool.ru"
    command = f'"{program_path}""%1"'
    
    try:
        add_to_context_menu(program_path, menu_name, command)
        print("Программа добавлена в контекстное меню!")
    except PermissionError:
        print("Запустите программу от имени администратора!")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
    input("Нажмите любую кнопку для выхода...")
    