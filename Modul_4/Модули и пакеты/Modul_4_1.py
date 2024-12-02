from fake_math import divide as fake_divide
from true_math import divide as true_divide

result_1 = fake_divide(69, 3)
result_2 = fake_divide(3, 0)
result_3 = true_divide(49, 7)
result_4 = true_divide(15, 0)
print(result_1)
print(result_2)
print(result_3)
print(result_4)  
