def apply_all_func(int_list, *functions):
    results = {}
    for i in functions:
        results[i.__name__] = i(int_list)
    return results

def c_min(int_list):
    return min(int_list)

def c_max(int_list):
    return max(int_list)

def c_len(int_list):
    return len(int_list)

def c_sum(int_list):
    return sum(int_list)

def c_sorted(int_list):
    return sorted(int_list)

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))

