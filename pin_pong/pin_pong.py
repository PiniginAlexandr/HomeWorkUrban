import pygame


class Ball:
    def __init__(self):
        self.ball = super().__init__('Ball.png', 0.05)
        # self.ball = pygame.image.load('Ball.png')


class Bar:
    def __init__(self):
        self.bar = super().__init__('Bar.png', 0.2)
        # self.bar = pygame.image.load('Bar.png')


class Game:
    def __init__(self, width=600, height=800):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('PinPong')
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            pygame.display.flip()

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()
