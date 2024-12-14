import math


class Figure:
    sides_count = 0

    def __init__(self, __color, *sides):
        self.__color = list(__color)
        self.filled = False
        if len(sides) == self.sides_count:
            self.__sides = list(sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return all(isinstance(side, int) and side > 0 for side in args) and len(args) == self.sides_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __color, radius):
        super().__init__(__color, radius)
        self.__radius = radius

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, radius):
        super().set_sides(radius)
        self.__radius = radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __color, a, b=None, c=None):
        if b is None or c is None:
            b = c = a
        super().__init__(__color, a, b, c)

    def get_square(self):
        # s = /p(p-a)(p-b)(p-c)
        # p = 1/2 * (a + b + c)
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, __color, edge_length):
        super().__init__(__color)
        self.set_sides(*([edge_length] * self.sides_count))

    def get_volume(self):
        edge_lenght = self.get_sides()[0]
        return edge_lenght ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())
# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())
# Проверка периметра (круга), это и есть длина:
print(len(circle1))
# Проверка объёма (куба):
print(cube1.get_volume())
