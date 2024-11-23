from walls import Walls
from paddle import Paddle

class Ball:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.y_speed = 10
        self.x_speed = 0

    #print ball position
    def __str__(self):
        return f'Ball is in {self.x}, {self.y}'

    #move the ball
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed

    #check if ball hits walls
    def hit_wall(self,left_wall: Walls, right_wall: Walls,upper_wall: Walls):
        if self.x <= left_wall.x:
            self.x_speed = -self.x_speed
            print('Hit left Wall')
        elif self.x >= right_wall.x:
            self.x_speed = -self.x_speed
            print('Hit right Wall')
        elif self.y <= left_wall.y:
            self.y_speed = -self.y_speed
            print('Hit upper Wall')

    #check if ball hit paddle
    def hit_paddle(self,paddle: Paddle):
        if self.x <= (paddle.center_x - paddle.width//2) and self.y >= (paddle.center_y):
            self.y_speed = -self.y_speed
            print('Hit paddle!')
            print('Return angle is x degrees')
        elif self.x >= (paddle.width//2 - paddle.center_x) and self.y >= paddle.center_y:
            self.y_speed = -self.y_speed
            print('Hit paddle!')
            print('Return angle is x degrees')
        elif self.y >= paddle.center_y:
            print('Paddle Miss')




