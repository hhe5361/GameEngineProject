from abc import ABC, abstractmethod
from typing import List
from pygame import Rect
import pygame
class Transform:
    def __init__(self, x=0, y=0, width=20, height=20):
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    @property
    def center(self):
        center_x = self.x + self.width / 2
        center_y = self.y + self.height / 2
        return center_x, center_y

    def change_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def change_dimension(self, new_width, new_height):
        self.width = new_width
        self.height = new_height

class MotionInfo:
    def __init__(self, transform: Transform, initial_velocity=(0, 0), initial_angle=0, initial_acceleration=(0, 0)):
        self.transform = transform
        self.velocity = list(initial_velocity)
        self.angle = initial_angle
        self.acceleration = list(initial_acceleration)

    def set_velocity(self, vx, vy):
        self.velocity = [vx, vy]

    def set_angle(self, angle):
        self.angle = angle

    def set_acceleration(self, ax, ay):
        self.acceleration = [ax, ay]

    def update_motion(self, d):
        self.velocity[0] += self.acceleration[0] * d
        self.velocity[1] += self.acceleration[1] * d

        self.transform.change_position(
            self.transform.x + self.velocity[0] * d,
            self.transform.y + self.velocity[1] * d
        )
        # print("moition : " +  self.transform.x)
        # print("moition : " + self.transform.y.__str__)

class AbstractGameObject(ABC):

    def __init__(self, transform: Transform, tag: List[str] = None, name: str = None):
        self.__transform__ = transform or Transform()
        self.__tag__ = tag or []
        self.__name__ = name
        self.__motion__ = MotionInfo(self.__transform__)

    @property
    def rect(self):
        return Rect(self.transform.x, self.transform.y, self.transform.width, self.transform.height)
    
    @property
    def transform(self):
        return self.__transform__

    @property
    def tag(self):
        return self.__tag__

    @property
    def name(self):
        return self.__name__
    
    @property
    def motion(self):
        return self.__motion__
    
    @abstractmethod
    def input(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    
    @abstractmethod
    def render(self):
        pass
    
    @abstractmethod
    def is_colliding_with(self, other_object):
        pass

    @abstractmethod
    def get_vertices(self):
        pass


class GameObject(AbstractGameObject):
    def __init__(self, transform: Transform, tags: List[str] = None, name: str = None):
        super().__init__(transform=transform, tag=tags, name=name)


    def get_vertices(self):
        return [
            (self.transform.x, self.transform.y),
            (self.transform.x + self.transform.width, self.transform.y),
            (self.transform.x, self.transform.y + self.transform.height),
            (self.transform.x + self.transform.width, self.transform.y + self.transform.height)
        ]

    @property
    def transform(self):
        return self.__transform__

    @property
    def tag(self):
        return self.__tag__

    @property
    def name(self):
        return self.__name__

    @property
    def motion(self):
        return self.__motion__
    
    def input(self):
        pass

    def is_colliding_with(self, other_object):
        pass

    def update(self, delta_time):
        super().motion.update_motion(delta_time)

    def render(self, screen, rgb,tagname = False):
        rect = super().rect
        pygame.draw.rect(screen, rgb, rect)

        if(tagname and (self.name is not None)):
            font = pygame.font.Font(None, 36)
            text = font.render(self.name, True, (0, 0, 0))
            text_rect = text.get_rect(center=(self.transform.center))
            screen.blit(text, text_rect)
        