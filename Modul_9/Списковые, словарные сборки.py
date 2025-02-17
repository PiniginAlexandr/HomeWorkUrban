first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) > 5]
second_result = [(y, x) for x in second_strings for y in first_strings if len(x) == len(y) and len(y) == len(x)]
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
