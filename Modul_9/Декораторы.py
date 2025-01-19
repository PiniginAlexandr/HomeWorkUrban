def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result > 1:
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    print('Число составное')
                    return result
            print('Число простое')
        else:
            print('Число составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    count = sum(args)
    return count


result = sum_three(2, 3, 6)
print(result)