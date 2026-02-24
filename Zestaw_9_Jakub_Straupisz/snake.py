import pygame
import random
import sys

# ===== STAŁE =====
GRID_W = 20
GRID_H = 15
CELL = 20
WIDTH = GRID_W * CELL
HEIGHT = GRID_H * CELL

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED   = (255, 0, 0)
BLUE  = (0, 0, 255)
GRAY  = (120, 120, 120)

UP    = [0, -1]
DOWN  = [0,  1]
LEFT  = [-1, 0]
RIGHT = [1,  0]

GOOD = 0
BAD  = 1

OBSTACLE_COUNT = 10

# ===== INIT =====
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake")
clock = pygame.time.Clock()

# ===== STAN GRY =====
snake = [[10, 7]]
direction = RIGHT
score = 0
game_over = False

# ----- PRZESZKODY -----
obstacles = []
while len(obstacles) < OBSTACLE_COUNT:
    pos = [random.randint(0, GRID_W-1), random.randint(0, GRID_H-1)]
    if pos not in obstacles and pos not in snake:
        obstacles.append(pos)

# ----- OWOC -----
def spawn_fruit():
    while True:
        pos = [random.randint(0, GRID_W-1), random.randint(0, GRID_H-1)]
        if pos not in snake and pos not in obstacles:
            return pos

fruit_pos = spawn_fruit()
fruit_type = random.choice([GOOD, BAD])
fruit_timer = 20

# ===== PĘTLA GRY =====
running = True
while running and not game_over:

    # --- ZDARZENIA ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                new_dir = UP
            elif event.key == pygame.K_DOWN:
                new_dir = DOWN
            elif event.key == pygame.K_LEFT:
                new_dir = LEFT
            elif event.key == pygame.K_RIGHT:
                new_dir = RIGHT
            else:
                new_dir = direction

            # zakaz ruchu wstecz
            if new_dir[0] != -direction[0] or new_dir[1] != -direction[1]:
                direction = new_dir
            else:
                game_over = True

    # --- RUCH WĘŻA ---
    new_head = [
        snake[0][0] + direction[0],
        snake[0][1] + direction[1]
    ]

    # ściana
    if (new_head[0] < 0 or new_head[0] >= GRID_W or
        new_head[1] < 0 or new_head[1] >= GRID_H):
        game_over = True
        break

    # przeszkoda
    if new_head in obstacles:
        game_over = True
        break

    snake.insert(0, new_head)

    # --- OWOC ---
    fruit_timer -= 1
    if fruit_timer <= 0:
        fruit_pos = spawn_fruit()
        fruit_type = random.choice([GOOD, BAD])
        fruit_timer = 20

    if new_head == fruit_pos:

        if fruit_type == GOOD:
            score += 1
            # brak pop → wzrost

        else:  # BAD
            if len(snake) > 2:
                snake.pop()
                snake.pop()
            else:
                game_over = True

        fruit_pos = spawn_fruit()
        fruit_type = random.choice([GOOD, BAD])
        fruit_timer = 20

    else:
        snake.pop()

    # --- RYSOWANIE ---
    screen.fill(BLACK)

    for obs in obstacles:
        pygame.draw.rect(
            screen,
            GRAY,
            (obs[0]*CELL, obs[1]*CELL, CELL, CELL)
        )

    for segment in snake:
        pygame.draw.rect(
            screen,
            GREEN,
            (segment[0]*CELL, segment[1]*CELL, CELL, CELL)
        )

    fruit_color = RED if fruit_type == GOOD else BLUE
    pygame.draw.rect(
        screen,
        fruit_color,
        (fruit_pos[0]*CELL, fruit_pos[1]*CELL, CELL, CELL)
    )

    pygame.display.flip()
    clock.tick(10)

# ===== KONIEC =====
pygame.quit()
print("GAME OVER")
print("Wynik:", score)
sys.exit()
