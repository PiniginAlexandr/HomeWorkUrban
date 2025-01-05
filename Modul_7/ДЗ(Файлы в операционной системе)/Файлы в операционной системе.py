import os
import time

directory = os.getcwd()
for root, dirs, files in os.walk(directory):
    for file in files:
        file_path = os.path.join(root, file)
        file_time = os.path.getmtime(file_path)
        formatted_time = time.strftime('%d.%m.%Y %H:%M:%S', time.localtime(file_time))
        file_size = os.path.getsize(file_path)
        parent_dir = os.path.dirname(file_path)
        print(f'Обнаружен файл: {file};'
              f'\nПуть: {file_path};'
              f'\nРазмер: {file_size} байт;'
              f'\nВремя изменения: {formatted_time};'
              f'\nРодительская дириктория: {parent_dir}.')

# Вывод:
# Обнаружен файл: Файлы в операционной системе.py;
# Путь: C:\Users\Shilk\PycharmProjects\HomeWorkUrban\Modul_7\ДЗ(Файлы в операционной системе)\Файлы в операционной системе.py;
# Размер: 1246 байт;
# Время изменения: 05.01.2025 16:41:37;
# Родительская дириктория: C:\Users\Shilk\PycharmProjects\HomeWorkUrban\Modul_7\ДЗ(Файлы в операционной системе).