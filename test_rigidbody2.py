import pygame
import sys
from pygame.locals import QUIT
from Object.GameObject import Transform, GameObject
from Physics.PhysicsEngine import RigidBody, CollisionDetection, ImpulsiveCollisionResponse
import random

BLUE = (0, 0, 255)
RED = (255, 0, 0)

pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RigidBody Collision Simulation")
pygame.time.delay(5000)

clock = pygame.time.Clock() 

rigidbody = []
for i in range(5):
    sety = 100 * (i+1)
    mass1 = random.randint(20,100)
    mass2 = random.randint(20,100)

    rigid_body = RigidBody(transform=Transform(x=200, y=sety, width=50, height=50), tags=[("rigid_body_object%d",i)], name="mass = {}".format(mass1), mass=mass1)
    rigid_body2 = RigidBody(transform=Transform(x=600, y=sety, width=50, height=50), tags=[("rigid_body_object%d",i)], name="mass = {}".format(mass2), mass=mass2)
    print(rigid_body)
    testset = [rigid_body,rigid_body2]
    rigidbody.append(testset)

collision_response = ImpulsiveCollisionResponse()
for obj in rigidbody:
    obj[0].motion.set_velocity((random.randint(30,100)),0)
    obj[1].motion.set_velocity((random.randint(-100,-30)),0)
print(rigidbody)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    delta_time = clock.tick(60) / 1000.0 

    for object in rigidbody:
        for obj in object:
            obj.update(delta_time)

    for object in rigidbody:
        if(CollisionDetection.sat_algorithm(object[0],object[1])):
            print("collision detection")
            collision_response.handle_collision(object[0],object[1])

    screen.fill((255, 255, 255))
    
    for object in rigidbody:
        object[0].render(screen, (0,0,255),True)
        object[1].render(screen,(255,0,0),True)
    
    pygame.display.update()
