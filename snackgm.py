# Import required libraries
import pygame          # Game engine for graphics, input, timing
import random          # Used to place apple randomly
import time            # Used for time-based mechanics
import sys             # Used to exit program safely

# Initialize all pygame modules
pygame.init()

# ================= SETTINGS =================

SIZE = 600             # Width and height of the game window (square)
RADIUS = 10            # Radius of snake and apple circles
STEP = RADIUS * 2      # Distance between grid cells (circle diameter)
GRID = SIZE // STEP    # Number of grid cells per row/column

BASE_SPEED = 150       # Normal movement speed in milliseconds
FAST_SPEED = 100       # Faster speed after 60 seconds
STARVE_TIME = 20       # Time before snake starts shrinking

# ================= WINDOW ==================

# Create game window
screen = pygame.display.set_mode((SIZE, SIZE))

# Set window title
pygame.display.set_caption("Snake Circle Game")

# Clock to control frame rate
clock = pygame.time.Clock()

# Font used for text
font = pygame.font.SysFont(None, 36)

# ================= COLORS ==================

DARK = (30, 30, 30)    # Dark square color
LIGHT = (60, 60, 60)   # Light square color
GREEN = (0, 200, 0)    # Snake color
RED = (200, 0, 0)      # Apple color
WHITE = (255, 255, 255)# Text color

# Custom event for snake movement
MOVE_EVENT = pygame.USEREVENT + 1

# ================= HELPERS =================

# Draw text centered horizontally at given y position
def draw_center(text, y):
    img = font.render(text, True, WHITE)     # Render text
    rect = img.get_rect(center=(SIZE // 2, y))
    screen.blit(img, rect)                   # Draw text

# Draw chessboard-style background
def draw_chess_bg():
    for row in range(GRID):
        for col in range(GRID):
            # Alternate colors like chessboard
            color = DARK if (row + col) % 2 == 0 else LIGHT
            pygame.draw.rect(
                screen,
                color,
                (col * STEP, row * STEP, STEP, STEP)
            )

# Convert grid position to pixel center
def grid_to_pixel(pos):
    col, row = pos
    return (
        col * STEP + RADIUS,
        row * STEP + RADIUS
    )

# Generate random apple position on grid
def spawn_apple():
    return (
        random.randint(0, GRID - 1),
        random.randint(0, GRID - 1)
    )

# ================= SCREENS =================

# Start screen before game begins
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
                return   # Start game

# Game over screen after losing
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
                    return   # Restart game
                if e.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()

# ================= GAME LOOP =================

def game_loop():
    # Initial snake position (center of grid)
    snake = [(GRID // 2, GRID // 2)]

    # Initial direction (no movement)
    direction = (0, 0)

    # Spawn first apple
    apple = spawn_apple()

    # Time tracking
    last_eat_time = time.time()
    start_time = time.time()

    # Set initial speed
    speed = BASE_SPEED
    pygame.time.set_timer(MOVE_EVENT, speed)

    while True:
        draw_chess_bg()

        # Increase speed after 60 seconds
        if time.time() - start_time > 60 and speed != FAST_SPEED:
            speed = FAST_SPEED
            pygame.time.set_timer(MOVE_EVENT, speed)

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Handle direction input
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_UP:
                    direction = (0, -1)
                elif e.key == pygame.K_DOWN:
                    direction = (0, 1)
                elif e.key == pygame.K_LEFT:
                    direction = (-1, 0)
                elif e.key == pygame.K_RIGHT:
                    direction = (1, 0)

            # Move snake on timer event
            if e.type == MOVE_EVENT and direction != (0, 0):
                hx, hy = snake[0]                  # Current head
                nx = hx + direction[0]             # New x
                ny = hy + direction[1]             # New y
                snake.insert(0, (nx, ny))           # Add new head

                # Wall collision
                if nx < 0 or nx >= GRID or ny < 0 or ny >= GRID:
                    return

                # Apple eaten
                if (nx, ny) == apple:
                    apple = spawn_apple()
                    last_eat_time = time.time()
                else:
                    snake.pop()                     # Remove tail

        # Starvation logic
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

        # Update display and limit FPS
        pygame.display.flip()
        clock.tick(60)

# ================= MAIN =================

# Game flow controller
while True:
    start_screen()
    game_loop()
    game_over_screen()
