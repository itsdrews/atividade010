

class Paddle:
    def __init__(self,center_x,center_y,width,height):
        self.width = width
        self.height = height
        self.center_x = center_x
        self.center_y = center_y
        self.color = 'Blue'
        self.speed = None

    def __str__(self):
        return f'Paddle is in {self.center_x - self.width//2} to {self.center_x + self.width//2}'

