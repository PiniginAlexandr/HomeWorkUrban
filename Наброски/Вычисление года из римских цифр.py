def solution(roman: str) -> int:
    num_list = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }
    year, prev_value = 0, 0
    for i in reversed(roman):
        value = num_list[i]
        if value < prev_value:
            year -= value
        else:
            year += value

        prev_value = value

    return year


print(solution('XL'))
