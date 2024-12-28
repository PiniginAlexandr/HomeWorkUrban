from pprint import pprint

name = 'sample2.txt'
file = open(name, 'r') # r - read(чтение), w - write(написать), a - append(добавить)
print(file.tell()) # Режим tell - показывает курсор(для чтения "|")
pprint(file.read())
print(file.seek(9)) # Режим seek - для сдвига курсора (tell)
pprint(file.read())
file.close()