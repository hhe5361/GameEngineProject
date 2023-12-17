import pygame
import random

class Particle:
    def __init__(self, position, speed, angle, lifetime, color:set):
        self.position = pygame.math.Vector2(position)
        self.speed = speed
        self.angle = angle
        self.lifetime = lifetime
        self.color = color

    def update(self, delta_time):
        if self.lifetime > 0:  # lifetime이 0 이상인 경우에만 업데이트
            velocity = pygame.math.Vector2(self.speed, 0).rotate(self.angle)
            self.position += velocity * delta_time * 0.2
            self.lifetime -= delta_time

    def render(self, screen):
        if self.lifetime > 0:  # lifetime이 0 이상인 경우에만 렌더링
            pygame.draw.circle(screen, self.color, (int(self.position.x), int(self.position.y)), 2)


class ParticleSystem:
    def __init__(self, position, num_particles,color : set):
        self.particles = []
        self.magicparticles = [] #없애도 되는데 그냥 넣어보고 싶어서 넣음.
        for _ in range(num_particles):
            speed = random.uniform(50, 200)
            angle = random.uniform(0, 360)
            lifetime = random.uniform(1, 3)
            particle = Particle(position, speed, angle, lifetime,color=color)
            magicparticle = Particle(position, speed, angle, lifetime,color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            self.particles.append(particle)

    def update(self, delta_time):
        for particle in self.particles:
            particle.update(delta_time)
        self.particles = [p for p in self.particles if p.lifetime > 0]

    def render(self, screen):
        for particle in self.particles:
            particle.render(screen)
