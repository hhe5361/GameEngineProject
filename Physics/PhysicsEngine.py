import pygame
import random
import math
from pygame import Rect
from Object.GameObject import GameObject,AbstractGameObject,Transform

class CollisionDetection:
    @staticmethod
    def sat_algorithm(obj1: AbstractGameObject, obj2: AbstractGameObject):
        axes = CollisionDetection.get_axes(obj1) + CollisionDetection.get_axes(obj2)

        delta = [obj2.transform.center[i] - obj1.transform.center[i] for i in range(2)]

        for axis in axes:
            projection1 = CollisionDetection.project(obj1, axis)
            projection2 = CollisionDetection.project(obj2, axis)

            if not CollisionDetection.overlap(projection1, projection2):
                return False
            
        return True

    @staticmethod
    def get_axes(obj: AbstractGameObject):
        return [(1, 0), (0, 1)]

    @staticmethod
    def project(obj: AbstractGameObject, axis):
        vertices = obj.get_vertices()

        projections = [vertex[0] * axis[0] + vertex[1] * axis[1] for vertex in vertices]

        return min(projections), max(projections)

    @staticmethod
    def overlap(projection1, projection2):
        return max(projection1[0], projection2[0]) <= min(projection1[1], projection2[1])

class RigidBody(GameObject):
    def __init__(self, transform: Transform, tags: list[str] = [], name: str = None, mass: int =30):
        super().__init__(transform=transform, tags=tags, name=name)
        self.rigid_body = mass

    #힘 적용
    def apply_force(self, force):
        acceleration = [force[0] / self.rigid_body, force[1] / self.rigid_body]
        super().motion.set_acceleration(*acceleration)
    
    #물 
    def apply_buoyancy(self, water_level, buoyancy=50, gravity=150):
        if self.transform.y + self.transform.height < water_level:
        # 물에 잠긴 깊이 계산
            submerged_depth = water_level - (self.transform.y + self.transform.height)
        
        # 부력 계산 (아래 방향으로 작용하므로 y 축에 부력을 적용)
            buoyancy_force = [0, self.rigid_body * buoyancy * submerged_depth]
        
        # 중력 계산 (아래 방향으로 작용하므로 y 축에 중력을 적용)
            gravity_force = [0, self.rigid_body * gravity]

        # 부력과 중력을 함께 적용하여 총 힘 계산
            total_force = [buoyancy_force[0] - gravity_force[0], buoyancy_force[1] - gravity_force[1]]

        # 총 힘을 RigidBody에 적용
            self.apply_force(total_force)

    #중력
    def apply_gravity(self, gravity=150):
        gravity_force = [0, self.rigid_body * gravity]
        self.apply_force(gravity_force)


class ImpulsiveCollisionResponse:
    def handle_collision(self, obj1: RigidBody, obj2: RigidBody):
        # 충돌 후의 속도 계산
        self.resolve_collision(obj1, obj2)

    def resolve_collision(self, obj1: RigidBody, obj2: RigidBody):
        normal = pygame.math.Vector2(obj2.transform.center[0] - obj1.transform.center[0],
                                      obj2.transform.center[1] - obj1.transform.center[1]).normalize()

        relative_velocity = pygame.math.Vector2(obj2.motion.velocity[0] - obj1.motion.velocity[0],
                                                obj2.motion.velocity[1] - obj1.motion.velocity[1])

        relative_speed_along_normal = normal.dot(relative_velocity)

        # 음수 relative_speed_along_normal은 충돌이 없는 상태
        if relative_speed_along_normal > 0:
            return

        # 반동 계산
        e = 1  # 탄성 계수 (1: 완전 탄성 충돌)
        j = -(1 + e) * relative_speed_along_normal
        j /= 1 / obj1.rigid_body + 1 / obj2.rigid_body

        impulse = [j * normal[0], j * normal[1]]

        # RigidBody에 반동 적용
        obj1.motion.set_velocity(obj1.motion.velocity[0] - impulse[0] / obj1.rigid_body,
                                 obj1.motion.velocity[1] - impulse[1] / obj1.rigid_body)

        obj2.motion.set_velocity(obj2.motion.velocity[0] + impulse[0] / obj2.rigid_body,
                                 obj2.motion.velocity[1] + impulse[1] / obj2.rigid_body)
