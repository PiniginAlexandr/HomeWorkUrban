import pygame
import random

# Определяем размеры окна и сетки
WIDTH, HEIGHT = 400, 900 #Или можно поставить своё разрешение
GRID_SIZE = 30
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Определяем цвета
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),  # Cyan
    (255, 165, 0),  # Orange
    (0, 0, 255),  # Blue
    (255, 0, 0),  # Red
    (128, 0, 128),  # Purple
    (0, 255, 0),  # Green
    (255, 255, 0)  # Yellow
]

# Определяем формы тетромино
SHAPES = [
    [[1], [1], [1], [1]],  # I
    [[1, 1], [1, 1]],  # O
    [[0, 1], [1, 1], [1]],  # L
    [[1, 1, 1], [0, 0, 1]],  # J
    [[0, 1], [0, 1], [1, 1]],  # S
    [[1, 0], [1, 1], [0, 1]],  # Z
    [[0, 1], [1, 1], [0, 0]]  # T
]


class Tetris:
    def __init__(self):
        self.board = [[0] * GRID_WIDTH for _ in range(GRID_HEIGHT)]
        self.current_piece = self.new_piece()
        self.next_piece = self.new_piece()
        self.game_over = False

    def new_piece(self):
        shape = random.choice(SHAPES)
        color = COLORS[SHAPES.index(shape)]
        return {'shape': shape, 'color': color,
                'x': GRID_WIDTH // 2 - len(shape[0]) // 2,
                'y': 0}

    def rotate_piece(self):
        self.current_piece['shape'] = list(zip(*self.current_piece['shape'][::-1]))

    def valid_position(self):
        for y in range(len(self.current_piece['shape'])):
            for x in range(len(self.current_piece['shape'][y])):
                if self.current_piece['shape'][y][x]:
                    if (x + self.current_piece['x'] < 0 or
                            x + self.current_piece['x'] >= GRID_WIDTH or
                            y + self.current_piece['y'] >= GRID_HEIGHT or
                            self.board[y + self.current_piece['y']][x + self.current_piece['x']] != 0):
                        return False
        return True

    def merge_piece(self):
        for y in range(len(self.current_piece['shape'])):
            for x in range(len(self.current_piece['shape'][y])):
                if self.current_piece['shape'][y][x]:
                    self.board[y + self.current_piece['y']][x + self.current_piece['x']] = self.current_piece['color']

    def clear_lines(self):
        lines_to_clear = []
        for i in range(GRID_HEIGHT):
            if all(self.board[i]):
                lines_to_clear.append(i)
        for i in lines_to_clear:
            del self.board[i]
            self.board.insert(0, [0] * GRID_WIDTH)

    def drop(self):
        if not self.game_over:
            self.current_piece['y'] += 1
            if not self.valid_position():
                self.current_piece['y'] -= 1
                self.merge_piece()
                self.clear_lines()
                self.current_piece = self.next_piece
                self.next_piece = self.new_piece()
                if not self.valid_position():
                    print("Game Over!")  # Отладка: вывод сообщения о конце игры.
                    self.game_over = True


def draw_board(screen, board):
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            color = board[y][x] if board[y][x] != 0 else BLACK
            pygame.draw.rect(screen,
                             color,
                             (x * GRID_SIZE,
                              y * GRID_SIZE,
                              GRID_SIZE - 1,
                              GRID_SIZE - 1))


def main():
    pygame.init()

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Tetris")

    clock = pygame.time.Clock()

    tetris = Tetris()

    while not tetris.game_over:
        screen.fill(BLACK)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                tetris.game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.current_piece['x'] -= 1
                    if not tetris.valid_position():
                        tetris.current_piece['x'] += 1

                if event.key == pygame.K_RIGHT:
                    tetris.current_piece['x'] += 1
                    if not tetris.valid_position():
                        tetris.current_piece['x'] -= 1

                if event.key == pygame.K_DOWN:
                    tetris.drop()

                if event.key == pygame.K_UP:
                    tetris.rotate_piece()
                    if not tetris.valid_position():
                        tetris.rotate_piece()
                        tetris.rotate_piece()
                        tetris.rotate_piece()

        tetris.drop()

        draw_board(screen, tetris.board)

        for y in range(len(tetris.current_piece['shape'])):
            for x in range(len(tetris.current_piece['shape'][y])):
                if tetris.current_piece['shape'][y][x]:
                    color = tetris.current_piece['color']
                    pygame.draw.rect(screen,
                                     color,
                                     ((tetris.current_piece['x'] + x) * GRID_SIZE,
                                      (tetris.current_piece['y'] + y) * GRID_SIZE,
                                      GRID_SIZE - 1,
                                      GRID_SIZE - 1))

        pygame.display.flip()
        clock.tick(10)


if __name__ == "__main__":
    main()