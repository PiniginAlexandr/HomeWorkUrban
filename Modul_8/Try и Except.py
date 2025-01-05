def add_everything_up(a, b):
    try:
        if TypeError(a, b):
            a = str(a)
            b = str(b)
            return a + b
    except:
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
