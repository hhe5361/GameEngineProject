import pygame
import sys
from pygame.locals import QUIT

from Object.GameObject import  Transform, GameObject
from Physics.PhysicsEngine import CollisionDetection,RigidBody

RED = (255, 0, 0)
BLUE = (0, 0, 255)

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RigidBodyDynamics Test")
pygame.time.delay(5000)

obj2 = GameObject(transform=Transform(x=151, y=150, width=50, height=50), tags=["obj2"])
rigid_body_object = RigidBody(transform=Transform(x=200, y=150, width=50, height=50), tags=["rigid_body_object"],mass=100)
rigid_body_object.apply_gravity()
clock = pygame.time.Clock() 

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    delta_time = clock.tick(60) / 1000.0 

    rigid_body_object.update(delta_time) 

    screen.fill((255,255,255))
    
    rigid_body_object.render(screen, BLUE) 
    pygame.display.update()
