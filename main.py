# class Human:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         self.say_info()
#
#     def say_info(self):
#         print(f'Привет, меня зовут {self.name}, мне {self.age}')
#
#     def birthday(self):
#         self.age += 1
#         print('У меня день рождения')
#
#     def __str__(self):
#         return self.name
#
#     def __len__(self):
#         return self.age
#
#     def __lt__(self, other):
#         return self.age < other.age
#
#     def __gt__(self, other):
#         return self.age > other.age
#
#     def __eq__(self, other):
#         return self.name == other.name and self.age == self.age
#
#     def __bool__(self):
#         return bool(self.age)
#
#     def __del__(self):
#         print(f'{self.name} ушёл.')
#
#
# den = Human('Денис', 22)
# max = Human('Макс', 23)
# a = 6
# print(den)


