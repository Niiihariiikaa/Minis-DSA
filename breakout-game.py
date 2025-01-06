import pygame
from pygame.locals import *
from random import randrange as rnd

# Initialize pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60
paddle_speed = 10  # Speed of the paddle
ball_radius = 20
ball_speed = 6
ball_rect = int(ball_radius * 2 ** 0.5)
ball = pygame.Rect(rnd(ball_rect, SCREEN_WIDTH - ball_rect), SCREEN_HEIGHT // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Blocks
block_list = [pygame.Rect(10 + 120 * i, 10 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(rnd(30, 256), rnd(30, 256), rnd(30, 256)) for _ in range(10 * 4)]

# Paddle dimensions and position
paddle_w = 330
paddle_h = 35
paddle = pygame.Rect(SCREEN_WIDTH // 2 - paddle_w // 2, SCREEN_HEIGHT - paddle_h - 10, paddle_w, paddle_h)

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout Game")

# Clock to control the frame rate
clock = pygame.time.Clock()

def draw_gradient(surface, start_color, end_color, width, height, horizontal=False):
    """Draw a gradient on the given surface."""
    for i in range(width if horizontal else height):
        t = i / (width if horizontal else height)
        r = start_color[0] + (end_color[0] - start_color[0]) * t
        g = start_color[1] + (end_color[1] - start_color[1]) * t
        b = start_color[2] + (end_color[2] - start_color[2]) * t
        color = (int(r), int(g), int(b))
        if horizontal:
            pygame.draw.line(surface, color, (i, 0), (i, height))
        else:
            pygame.draw.line(surface, color, (0, i), (width, i))

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    # Clear the screen with a gradient
    draw_gradient(screen, (230, 190, 255), (255, 204, 229), SCREEN_WIDTH, SCREEN_HEIGHT // 3)
    draw_gradient(screen, (255, 204, 229), (255, 255, 204), SCREEN_WIDTH, SCREEN_HEIGHT // 3, horizontal=False)
    draw_gradient(screen, (255, 255, 204), (240, 230, 255), SCREEN_WIDTH, SCREEN_HEIGHT, horizontal=False)

    # Draw blocks
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)]

    # Draw the paddle
    pygame.draw.rect(screen, pygame.Color('pink'), paddle)

    # Draw the ball
    pygame.draw.circle(screen, pygame.Color('purple'), ball.center, ball_radius)
    ball.x += ball_speed * dx
    ball.y += ball_speed * dy

    # Ball collision with walls
    if ball.centerx < ball_radius or ball.centerx > SCREEN_WIDTH - ball_radius:
        dx = -dx
    if ball.centery < ball_radius:
        dy = -dy

    # Ball collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dy = -dy

    # Ball collision with blocks
    hit_index = ball.collidelist(block_list)
    if hit_index != -1:
        hit_block = block_list.pop(hit_index)
        color_list.pop(hit_index)

        # Adjust ball direction based on collision
        if abs(ball.centerx - hit_block.left) < ball_radius or abs(ball.centerx - hit_block.right) < ball_radius:
            dx = -dx
        else:
            dy = -dy

    # Check for game over
    if ball.top > SCREEN_HEIGHT:
        print("Game Over! You lost.")
        running = False

    # Check for win condition
    if not block_list:
        print("Congratulations! You cleared all blocks.")
        running = False

    # Move the paddle
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
        paddle.right += paddle_speed

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()
