import pygame
import random
import time
import sys

pygame.init()

# ================= SETTINGS =================
SIZE = 600
RADIUS = 10
STEP = RADIUS * 2
GRID = SIZE // STEP

BASE_SPEED = 150
FAST_SPEED = 100
STARVE_TIME = 20

# ================= WINDOW ==================
screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption("Snake Circle Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# ================= COLORS ==================
DARK = (30, 30, 30)
LIGHT = (60, 60, 60)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
WHITE = (255, 255, 255)

MOVE_EVENT = pygame.USEREVENT + 1

# ================= HELPERS =================
def draw_center(text, y):
    img = font.render(text, True, WHITE)
    rect = img.get_rect(center=(SIZE // 2, y))
    screen.blit(img, rect)

def draw_chess_bg():
    for row in range(GRID):
        for col in range(GRID):
            color = DARK if (row + col) % 2 == 0 else LIGHT
            pygame.draw.rect(
                screen,
                color,
                (col * STEP, row * STEP, STEP, STEP)
            )

def grid_to_pixel(pos):
    col, row = pos
    return (
        col * STEP + RADIUS,
        row * STEP + RADIUS
    )

def spawn_apple():
    return (
        random.randint(0, GRID - 1),
        random.randint(0, GRID - 1)
    )

# ================= SCREENS =================
def start_screen():
    while True:
        draw_chess_bg()
        draw_center("Snake Circle Game", 260)
        draw_center("Press ENTER to Start", 320)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN and e.key == pygame.K_RETURN:
                return

def game_over_screen():
    while True:
        draw_chess_bg()
        draw_center("GAME OVER", 260)
        draw_center("R = Replay   Q = Quit", 320)
        pygame.display.flip()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_r:
                    return
                if e.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# ================= GAME LOOP =================
def game_loop():
    snake = [(GRID // 2, GRID // 2)]
    direction = (0, 0)
    apple = spawn_apple()

    last_eat_time = time.time()
    start_time = time.time()

    speed = BASE_SPEED
    pygame.time.set_timer(MOVE_EVENT, speed)

    while True:
        draw_chess_bg()

        if time.time() - start_time > 60 and speed != FAST_SPEED:
            speed = FAST_SPEED
            pygame.time.set_timer(MOVE_EVENT, speed)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    direction = (0, -1)
                elif e.key == pygame.K_DOWN:
                    direction = (0, 1)
                elif e.key == pygame.K_LEFT:
                    direction = (-1, 0)
                elif e.key == pygame.K_RIGHT:
                    direction = (1, 0)

            if e.type == MOVE_EVENT and direction != (0, 0):
                hx, hy = snake[0]
                nx = hx + direction[0]
                ny = hy + direction[1]
                snake.insert(0, (nx, ny))

                if nx < 0 or nx >= GRID or ny < 0 or ny >= GRID:
                    return

                if (nx, ny) == apple:
                    apple = spawn_apple()
                    last_eat_time = time.time()
                else:
                    snake.pop()

        if time.time() - last_eat_time > STARVE_TIME:
            if len(snake) > 1:
                snake.pop()
                last_eat_time = time.time()
            else:
                return

        # Draw apple
        pygame.draw.circle(
            screen,
            RED,
            grid_to_pixel(apple),
            RADIUS
        )

        # Draw snake
        for part in snake:
            pygame.draw.circle(
                screen,
                GREEN,
                grid_to_pixel(part),
                RADIUS
            )

        pygame.display.flip()
        clock.tick(60)

# ================= MAIN =================
while True:
    start_screen()
    game_loop()
    game_over_screen()
