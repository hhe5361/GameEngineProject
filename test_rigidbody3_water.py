import pygame
from Object.GameObject import Transform, MotionInfo
from Physics.PhysicsEngine import RigidBody,CollisionDetection,ImpulsiveCollisionResponse


pygame.init()

screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("부력 시뮬레이션 테스트")
pygame.time.delay(5000)

transform1 = Transform(x=100, y=180, width=30, height=30)
rigid_body1 = RigidBody(transform=transform1, tags=["object1"], name="Object 1", mass=30)

transform2 = Transform(x=200, y=200, width=30, height=30)
rigid_body2 = RigidBody(transform=transform2, tags=["object2"], name="Object 2", mass=30)

water_level = 300 
buoyancy_force = 5
def draw_water_level(surface, water_level):
    pygame.draw.line(surface, (0, 0, 255), (0, water_level), (screen_width, water_level), 2)

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    rigid_body1.apply_buoyancy(water_level, buoyancy=buoyancy_force)
    rigid_body2.apply_buoyancy(water_level, buoyancy=buoyancy_force)

    delta_time = clock.tick(60) / 1000.0

    rigid_body1.update(delta_time)
    rigid_body2.update(delta_time)

    screen.fill((255, 255, 255))

    draw_water_level(screen, water_level)

    rigid_body1.render(screen, (255, 0, 0))
    rigid_body2.render(screen, (0, 0, 255))

    pygame.display.flip()

pygame.quit()