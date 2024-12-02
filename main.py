class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.say_info()

    def say_info(self):
        print(f'Привет, меня зовут {self.name}, мне {self.age}')

    def birthday(self):
        self.age += 1
        print('У меня день рождения')

den = Human('Денис', 22)
max = Human('Макс', 23)

den.say_info()
max.say_info()

