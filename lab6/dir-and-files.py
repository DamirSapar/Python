#Exercise 1
import os
def list_items(path, mode="all"):
    if not os.path.exists(path):
        print("Указанный путь не существует.")
        return    
    if mode == "dirs":
        for root, dirs, files in os.walk(path, topdown=True):
            print("Каталоги в:", root)
            print(dirs)
    elif mode == "files":
        for root, dirs, files in os.walk(path, topdown=True):
            print("Файлы в:", root)
            print(files)
    elif mode == "all":
        for root, dirs, files in os.walk(path, topdown=True):
            print("Путь каталога:", root)
            print("Каталоги:", dirs)
            print("Файлы:", files)
    else:
        print("Неверный режим. Используйте 'dirs', 'files' или 'all'.")
path = input("Введите путь: ")
mode = input("Выберите режим (dirs/files/all): ")
list_items(path, mode)



#EXercise 2
import os
def check_path_access(path):
    if not os.path.exists(path):
        print("Путь не существует.")
        return
    print(f"Проверка пути: {path}")
    print(f"Существует: {'Да' if os.path.exists(path) else 'Нет'}")
    print(f"Читаемый: {'Да' if os.access(path, os.R_OK) else 'Нет'}")
    print(f"Записываемый: {'Да' if os.access(path, os.W_OK) else 'Нет'}")
    print(f"Исполняемый: {'Да' if os.access(path, os.X_OK) else 'Нет'}")
path = input("Введите путь для проверки: ")
check_path_access(path)



#Exercise 3
import os
def check_path_info(path):
    if not os.path.exists(path):
        print("Путь не существует.")
        return    
    print(f"Путь существует: {path}")
    print(f"Каталог: {os.path.dirname(path)}")
    print(f"Имя файла: {os.path.basename(path)}")
path = input("Введите путь для проверки: ")
check_path_info(path)



#Exercise 4
def count_lines_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            line_count = sum(1 for line in file)
        print(f"Количество строк в файле '{filename}': {line_count}")
    except FileNotFoundError:
        print("Файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
filename = input("Введите имя файла: ")
count_lines_in_file(filename)



#Exercise 5
def write_list_to_file(filename, data_list):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in data_list:
                file.write(str(item) + '\n')
        print(f"Список успешно записан в файл '{filename}'")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
data = ["яблоко", "банан", "вишня", "груша", "персик"]
filename = input("Введите имя файла для записи: ")
write_list_to_file(filename, data)



#Exercise 6
import string
def generate_text_files():
    for letter in string.ascii_uppercase:
        filename = f"{letter}.txt"
        try:
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(f"Это файл {filename}\n")
            print(f"Файл '{filename}' создан.")
        except Exception as e:
            print(f"Ошибка при создании файла '{filename}': {e}")
generate_text_files()



#Exercise 7
def copy_file(source, destination):
    try:
        with open(source, 'r', encoding='utf-8') as src_file:
            content = src_file.read()
        
        with open(destination, 'w', encoding='utf-8') as dest_file:
            dest_file.write(content)
        
        print(f"Содержимое файла '{source}' скопировано в '{destination}'")
    except FileNotFoundError:
        print("Исходный файл не найден.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")
source_file = input("Введите имя исходного файла: ")
destination_file = input("Введите имя файла назначения: ")
copy_file(source_file, destination_file)



#Exercise 8
import os
def delete_file(path):
    if not os.path.exists(path):
        print("Файл не существует.")
        return  
    if not os.access(path, os.W_OK):
        print("Нет прав на удаление файла.")
        return
    try:
        os.remove(path)
        print(f"Файл '{path}' успешно удалён.")
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")
file_path = input("Введите путь к файлу для удаления: ")
delete_file(file_path)