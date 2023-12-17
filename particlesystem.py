import pygame
import sys
from pygame.locals import QUIT
from Physics.Particles import Particle, ParticleSystem
import random  # 랜덤 모듈 추가

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Explosion Simulation")
pygame.time.delay(5000)

WHITE = (255, 255, 255)
explosions = [] 
num_explosions = 15

for _ in range(num_explosions):
    explosion_position = (random.randint(50, SCREEN_WIDTH - 50), random.randint(50, SCREEN_HEIGHT - 50))
    explosion = ParticleSystem(explosion_position, 100,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    explosions.append(explosion)

clock = pygame.time.Clock() 
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))

    delta_time = clock.tick(60) / 1000.0 

    for explosion in explosions:
        explosion.update(delta_time)
        explosion.render(screen)
    pygame.display.update()
