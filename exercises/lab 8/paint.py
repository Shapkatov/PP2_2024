import pygame
import sys

pygame.init()

# Constants
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
BG_COLOR = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (128, 128, 128)
COLORS = [BG_COLOR, BLACK, RED, GREEN, BLUE, YELLOW, CYAN, MAGENTA, GRAY]

# Variables
drawing = False
last_pos = None
radius = 10
color = BLACK
bg_color = BG_COLOR

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Paint")
screen.fill(BG_COLOR)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True
            last_pos = event.pos
        elif event.type == pygame.MOUSEBUTTONUP:
            drawing = False
        elif event.type == pygame.MOUSEMOTION:
            if drawing:
                if pygame.key.get_pressed()[pygame.K_LCTRL] or pygame.key.get_pressed()[pygame.K_RCTRL]:
                    pygame.draw.circle(screen, bg_color, event.pos, radius)
                else:
                    pygame.draw.circle(screen, color, event.pos, radius)
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                radius = 10
            elif event.key == pygame.K_c:
                color = COLORS[(COLORS.index(color) + 1) % len(COLORS)]
            elif event.key == pygame.K_e:
                color = bg_color
            elif event.key == pygame.K_ESCAPE:
                screen.fill(BG_COLOR)

    # Update the display
    pygame.display.flip()