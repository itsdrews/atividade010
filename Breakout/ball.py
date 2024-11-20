

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.y_speed = None
        self.x_speed = None

    def __str__(self):
        return f'Ball is in {self.x}, {self.y}'