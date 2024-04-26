import pygame
import random

pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
CELL_SIZE = 20
SNAKE_COLOR = (255, 0, 0)
BACKGROUND_COLOR = (70, 130, 180)

# Add more food types with different weights
FOOD_TYPES = [
    {'color': (0, 255, 0), 'weight': 0.6, 'disappear_time': 9000},  # Green food
    {'color': (255, 255, 0), 'weight': 0.3, 'disappear_time': 3000},  # Yellow food
    {'color': (255, 0, 255), 'weight': 0.1, 'disappear_time': 2000},  # Purple food
   
]

# Directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Game variables
snake = [(10, 10)]
snake_direction = RIGHT
food_positions = []
food_types = []
for _ in range(2):
    food, food_type = (5, 5), random.choices(FOOD_TYPES, [f['weight'] for f in FOOD_TYPES])[0]
    food_positions.append(food)
    food_types.append(food_type)
score = 0
level = 1
speed = 10

# Timer for disappearing food
disappear_timer = pygame.time.get_ticks()

# Game window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

# Game clock
clock = pygame.time.Clock()

# Functions
def draw_snake():
    for segment in snake:
        pygame.draw.rect(window, SNAKE_COLOR, (segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def draw_food():
    for i in range(len(food_positions)):
        pygame.draw.rect(window, food_types[i]['color'], (food_positions[i][0] * CELL_SIZE, food_positions[i][1] * CELL_SIZE, CELL_SIZE, CELL_SIZE))

def check_collision():
    if snake[0][0] < 0 or snake[0][0] >= WINDOW_WIDTH / CELL_SIZE or snake[0][1] < 0 or snake[0][1] >= WINDOW_HEIGHT / CELL_SIZE:
        return True
    if snake[0] in snake[1:]:
        return True
    return False       

def generate_food():
    food_positions = []
    food_types = []
    for _ in range(2):
        food_type = random.choices(FOOD_TYPES, [f['weight'] for f in FOOD_TYPES])[0]
        while True:
            x = random.randint(0, int(WINDOW_WIDTH / CELL_SIZE) - 1)
            y = random.randint(0, int(WINDOW_HEIGHT / CELL_SIZE) - 1)
            if (x, y) not in snake and (x, y) not in food_positions:
                food_positions.append((x, y))
                food_types.append(food_type)
                break
    return food_positions, food_types

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_direction != DOWN:
                snake_direction = UP
            elif event.key == pygame.K_DOWN and snake_direction != UP:
                snake_direction = DOWN
            elif event.key == pygame.K_LEFT and snake_direction != RIGHT:
                snake_direction = LEFT
            elif event.key == pygame.K_RIGHT and snake_direction != LEFT:
                snake_direction = RIGHT

    # Move the snake
    new_head = (snake[0][0] + snake_direction[0], snake[0][1] + snake_direction[1])
    snake = [new_head] + snake[:-1]

    # Check for collisions
    if check_collision():
        running = False

    # Check if the snake eats food
    for i, food in enumerate(food_positions):
        if snake[0] == food:
            snake.append(snake[-1])  # Grow the snake
            score += 1
            if score % 3 == 0:
                level += 1
                speed += 2

            food_positions.pop(i)  # Remove eaten food
            food_types.pop(i)  # Remove food type
            new_food_positions, new_food_types = generate_food()
            food_positions.extend(new_food_positions)  # Add new food positions
            food_types.extend(new_food_types)  # Add new food types

    # Update the disappearing food  
    for i, food in enumerate(food_positions):
        if pygame.time.get_ticks() - disappear_timer > food_types[i]['disappear_time']:
            food_positions.pop(i)  # Remove disappeared food
            food_types.pop(i)  # Remove food type
            new_food_positions, new_food_types = generate_food()
            food_positions.extend(new_food_positions)  # Add new food positions
            food_types.extend(new_food_types)  # Add new food types
            disappear_timer = pygame.time.get_ticks()

    # Draw everything
    window.fill(BACKGROUND_COLOR)
    draw_snake()
    draw_food()

    # Display score and level
    font = pygame.font.SysFont(None, 30)
    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    level_text = font.render(f"Level: {level}", True, (255, 255, 255))
    window.blit(score_text, (10, 10))
    window.blit(level_text, (10, 40))

    pygame.display.update()

    # Control game speed
    clock.tick(speed)

pygame.quit()