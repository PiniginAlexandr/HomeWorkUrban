def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [1, 'str', False]
values_dict = {'a': 1, 'b': 'str', 'c': True}

values_list_2 = [54.32, 'Строка']
values_dict_2 = {'c': False}
print('\n')
print_params(1, b=25)
print_params(c=[1, 2, 3])
print_params(a=41, b='str', c=False)
print_params(b=25)
print_params(c=10)
print_params() #Без аргументов
print('\n')
print_params(*values_list)
print_params(**values_dict)
print('\n')
print_params(*values_list_2, 42)
print_params(*values_list_2, **values_dict_2)
