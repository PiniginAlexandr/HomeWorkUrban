num_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list = []
ind = 0
while ind < len(num_list):
    if num_list[ind] < 0:
        break
    if num_list[ind] > 0:
        my_list.append(num_list[ind])
    ind += 1


print(f'Список положительных чисел : {my_list}')





