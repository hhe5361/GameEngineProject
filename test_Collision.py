
import pygame
import sys
from pygame.locals import QUIT, KEYDOWN, KEYUP, K_LEFT, K_RIGHT, K_UP, K_DOWN

from Physics.PhysicsEngine import CollisionDetection
from Physics.Particles import Particle,ParticleSystem
from Object.GameObject import AbstractGameObject, Transform, GameObject,MotionInfo

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collision Detection Test")
pygame.time.delay(3000)

clock = pygame.time.Clock() 

RED = (255, 0, 0)
BLUE = (0, 0, 255)

obj1 = GameObject(transform=Transform(x=100, y=100, width=50, height=50), tags=["obj1"])
obj2 = GameObject(transform=Transform(x=150, y=150, width=50, height=50), tags=["obj2"])

collision_detection = CollisionDetection()


class Player(GameObject):
    def __init__(self, transform: Transform, tags: list[str] = None, name: str = None):
        super().__init__(transform=transform, tags=tags, name=name)
        self.player_color = (0, 255, 0)  
        self.speed = 200  

    def update(self,delta_time):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.motion.set_velocity(-self.speed, 0)
        elif keys[pygame.K_RIGHT]:
            self.motion.set_velocity(self.speed, 0)
        elif keys[pygame.K_UP]:
            self.motion.set_velocity(0, -self.speed)
        elif keys[pygame.K_DOWN]:
            self.motion.set_velocity(0, self.speed)
        else:
            self.motion.set_velocity(0, 0)

        super().update(delta_time)

player = Player(transform=Transform(x=500, y=200, width=50, height=50), tags=["player"])

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    delta_time = clock.tick(60) / 1000.0 

    if collision_detection.sat_algorithm(player, obj1) or collision_detection.sat_algorithm(player, obj2):
        player.player_color = RED 
    else:
        player.player_color = (0, 255, 0) 

    player.update(delta_time) 


    screen.fill((255, 255, 255))

    player.render(screen,player.player_color)
    obj1.render(screen, BLUE)
    obj2.render(screen, BLUE)

    pygame.display.update()