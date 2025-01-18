def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        a, b = str(a), str(b)
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
result = add_everything_up(123.456, 7)
result = round(result, 3)
print(result)
