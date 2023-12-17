from Object.GameObject import GameObject, Transform

class SimpleAI(GameObject):
    def __init__(self, transform: Transform, tags=None, name=None, player : GameObject =None,speed : int = 100):
        super().__init__(transform=transform, tags=tags, name=name)
        self.simple_ai_data = None 
        self.player = player
        self.speed = speed

    def implement_simple_ai(self, delta_time, sight : int = 200):
        if self.player:
            distance_to_player = ((self.player.transform.x - self.transform.x) ** 2 +
                                  (self.player.transform.y - self.transform.y) ** 2) ** 0.5
            
            if distance_to_player <= sight:
                direction_x = self.player.transform.x - self.transform.x
                direction_y = self.player.transform.y - self.transform.y
                normalized_direction = (direction_x / distance_to_player, direction_y / distance_to_player)

                ai_velocity = (normalized_direction[0] * self.speed, normalized_direction[1] * self.speed)
                self.motion.set_velocity(ai_velocity[0], ai_velocity[1])
                self.motion.update_motion(delta_time)

