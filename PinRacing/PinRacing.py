import pygame
import random
import sys

# Разрешение экрана
width = 800
height = 619

# Создание игровой платформы
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('2D PinRacing')


class Car:
    def __init__(self, x, y):
        self.image = pygame.image.load('map/car.png')
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self, dx):
        self.x += dx


class Block:
    def __init__(self, x, y):
        self.image = pygame.image.load('map/car_block.png')
        self.x = x
        self.y = y

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))

    def move(self):
        self.y += 5  # Движение вниз


class Road:
    def __init__(self):
        self.image = pygame.image.load('map/road.png')  # Загружаем изображение дороги

    def draw(self, screen):
        screen.blit(self.image, (0, 0))  # Отрисовываем изображение дороги на экране


def collision(car, block):
    car_rect = pygame.Rect(car.x, car.y, car.image.get_width(), car.image.get_height())
    block_rect = pygame.Rect(block.x, block.y, block.image.get_width(), block.image.get_height())
    return car_rect.colliderect(block_rect)


running = True
score = 0

player_car = Car(400, 500)  # Создание экземпляра автомобиля
blocks = []  # Список блоков
block_spawn_time = 0  # Время для спавна блока
road = Road()  # Создание экземпляра дороги

# Основной игровой цикл
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_car.move(-5)
    if keys[pygame.K_RIGHT]:
        player_car.move(5)

    # Логика создания новых блоков
    block_spawn_time += 1  # Увеличиваем время спавна
    if block_spawn_time > 20:  # Каждые 20 кадров создаём новый блок
        new_block_x = random.randint(0, width - 50)  # Случайная позиция по X
        blocks.append(Block(new_block_x, -50))  # Создание нового блока выше экрана
        block_spawn_time = 0  # Сброс времени спавна

    for block in blocks[:]:  # Проходим по копии списка блоков
        block.move()
        if collision(player_car, block):
            print(f'Game over! Your score: {score}.')
            running = False

        if block.y > height:  # Если блок вышел за нижнюю границу экрана
            blocks.remove(block)  # Удаляем его из списка

    screen.fill((0, 0, 0))  # Очистка экрана (это можно убрать)

    road.draw(screen)  # Отрисовка дороги
    player_car.draw(screen)  # Отрисовка автомобиля

    for block in blocks:
        block.draw(screen)  # Отрисовка всех блоков

    pygame.display.flip()  # Обновление экрана

    score += 1  # Увеличиваем счёт за кадр (можно изменить логику)

    pygame.time.delay(20)  # Задержка для замедления цикла

pygame.quit()
sys.exit()