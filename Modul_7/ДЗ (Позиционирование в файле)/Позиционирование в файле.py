def custom_write(file_name, strings):
    string_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    for index, string in enumerate(strings):
        byte_positions = file.tell()
        file.write(string + '\n')
        string_positions[(index + 1, byte_positions)] = string
    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)