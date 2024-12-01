import pygame
import random
import sys

#Разрешение экрана
wight = 400
height = 600
gravity = 0.25
jump_strength = - 6

#Создание игровой платформы
pygame.init()
screen = pygame.display.set_mode((wight, height))
pygame.display.set_caption('Flappy Bird')

bird_image = pygame.image.load('assets/bird.png')
pipe_image_low = pygame.image.load('assets/pipelow.png')
pipe_image_down = pygame.image.load('assets/pipedown.png')
background_image = pygame.image.load('assets/background.png')


class Bird:
    def __init__(self):
        self.image = bird_image
        self.rect = self.image.get_rect(center=(100, height // 2))
        self.velocity = 0

    def jump(self):
        self.velocity = jump_strength

    def update(self):
        self.velocity += gravity
        self.rect.centery += self.velocity
        if self.rect.top < 0 or self.rect.bottom > height:  # Проверка на выход за границы карты
            pass

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Pipe:
    def __init__(self):
        self.image = pipe_image_low
        self.rect = self.image.get_rect(topleft=(wight, random.randint(150, height - 50)))
        self.image = pipe_image_down
        self.rect = self.image.get_rect(topleft=(wight, random.randint(-150, height - 50)))


    def update(self):
        self.rect.x -= 5  # Скорость движения труб

    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def off_screen(self):
        return self.rect.right < 0


def main():
    bird = Bird()
    pipes = [Pipe()]  # Список труб

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                bird.jump()

        # Обновление новых объектов после прохода
        bird.update()
        for pipe in pipes:
            pipe.update()
            if pipe.off_screen():
                pipes.remove(pipe)
                pipes.append(Pipe())  # Добавление новых труб

        # Отрисовка объектов на экране
        screen.blit(background_image, (0, 0))
        bird.draw(screen)
        for pipe in pipes:
            pipe.draw(screen)

        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Ограничение fps


if __name__ == '__main__':
    main()
