my_string = input('Введите текст: ')
print('Количество символом в строке:', len(my_string))
print(f'Строка в верхнем регистре: \n    {my_string.upper()}')
print(f'Строка в нижнем регистре: \n    {my_string.lower()}')
print(f'Удаление всех пробелов: \n    {my_string.replace(' ', '')}')
print(f'Первый символ строки: \n    {my_string[0]}')
print(f'Последний символ строки: \n    {my_string[-1]}')

