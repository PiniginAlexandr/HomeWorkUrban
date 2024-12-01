def get_multiplied_digits(number):
    str_number = str(number)
    first = str_number[0]
    if len(str_number) == 1:
        if str_number == '0':
            return 1
        return int(str_number)
    if len(str_number) > 1:
        return int(first) * get_multiplied_digits(int(str_number[1:]))
    else:
        return int(first)


result = get_multiplied_digits(402030)
print(result)
