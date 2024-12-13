class Vehicle:
    __COLOR_VARIANTS = ['blue', 'red', 'green', 'black', 'white']

    def __init__(self, owner, model, color, engine_power):
        self.owner = str(owner)
        self.__model = str(model)
        self.__engine_power = int(engine_power)
        self.__color = str(color)

    def get_model(self):
        return self.__model

    def get_horsepower(self):
        return self.__engine_power

    def get_color(self):
        return self.__color


class Sedan(Vehicle):
    def print_info(self):
        print(f'Модель: {self.get_model()} '
              f'\nМощность двигателя: {self.get_horsepower()} '
              f'\nЦвет: {self.get_color()} '
              f'\nВладелец: {self.owner}')

    def set_color(self, new_color):
        if new_color.lower() in self._Vehicle__COLOR_VARIANTS:
            self._Vehicle__color = str(new_color)
        else:
            print(f'Нельзя сменить {self.get_color()} на {new_color}.')


vehicle1 = Sedan('Fedos', 'Toyota Mark ||', 'blue', 500)
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()
