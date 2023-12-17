class Scene:
    def __init__(self):
        self.game_objects = []

    def add_game_object(self, game_object):
        self.game_objects.append(game_object)

    def update(self):
        for game_object in self.game_objects:
            game_object.input()
            game_object.update()

    def render(self, screen):
        screen.fill((255, 255, 255))
        for game_object in self.game_objects:
            game_object.render(screen, (255, 0, 0))
