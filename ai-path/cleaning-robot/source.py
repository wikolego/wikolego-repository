import os
os.environ["SDL_AUDIODRIVER"] = "dummy"

import pygame
import random

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Autonomous Robot Simulation")

clock = pygame.time.Clock()

x = WIDTH // 2
y = HEIGHT // 2
radius = 20

vx = random.choice([-4, -3, 3, 4])
vy = random.choice([-4, -3, 3, 4])

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += vx
    y += vy

    if x <= radius or x >= WIDTH - radius:
        vx *= -1
    if y <= radius or y >= HEIGHT - radius:
        vy *= -1

    screen.fill((20, 20, 20))

    pygame.draw.circle(screen, (0, 200, 0), (x, y), radius)

    pygame.draw.line(screen, (255, 255, 255), (x, y), (x + vx * 5, y + vy * 5), 2)

    pygame.display.flip()

pygame.quit()