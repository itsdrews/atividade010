from ball import Ball
from walls import Walls
from score import Score
from blocks import Blocks
from paddle import Paddle
from random import randint

#GAME SETTINGS
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_HEIGHT = 20
PADDLE_WIDTH = 40
PADDLE_CENTER_X = WINDOW_WIDTH //2
PADDLE_CENTER_Y = WINDOW_HEIGHT - 100
BALL_RADIUS = 2
BALL_COLOR = 'white'
BALL_CENTER_X = WINDOW_WIDTH //2
BALL_CENTER_Y = WINDOW_HEIGHT - PADDLE_HEIGHT
BALL_SPEED = 6



class Game:
    def __init__(self):
        self.running = False
        self.idle = True

    #draw all screen objects
    def create_screen_objects(self,ball : Ball,left_wall:Walls,right_wall:Walls,
                              uper_wall: Walls,paddle:Paddle,blocks:Blocks):

        ball = Ball(x=randint(0, WINDOW_WIDTH), y=randint(200, WINDOW_HEIGHT), radius=BALL_RADIUS, color=BALL_COLOR)
        left_wall = Walls(x=10, y=0, width=10, height=WINDOW_HEIGHT)
        right_wall = Walls(x=700, y=0, width=10, height=WINDOW_HEIGHT)
        upper_wall = Walls(x=0, y=0, width=WINDOW_WIDTH, height=10)
        if self.idle == False:
            paddle = Paddle(center_x=PADDLE_CENTER_X, center_y=PADDLE_CENTER_Y, width=PADDLE_WIDTH, height=PADDLE_HEIGHT)
        else:
            paddle = Paddle(center_x=PADDLE_CENTER_X, center_y=PADDLE_CENTER_Y, width=WINDOW_WIDTH, height=PADDLE_HEIGHT)
        blocks = Blocks()

        return [ball,left_wall,right_wall,upper_wall,paddle,blocks]

    #runs the game
    def start(self):
        self.running = True
        self.idle = False
        while self.running:
            print("game is running")


    #runs idle screen while not playing
    def idle_screen(self):
        screen = self.create_screen_objects(Ball,Walls,Walls,Walls,Paddle,Blocks)
        left_wall = screen[1]
        right_wall = screen[2]
        upper_wall = screen[3]
        paddle = screen[4]
        self.running = True
        a = 0
        ball = screen[0]
        while self.running:
            ball.move()
            ball.hit_wall(left_wall, right_wall, upper_wall)
            print(ball)
            ball.hit_paddle(paddle)
            a += 1
            if a == 100:
                self.stop()

    #closes the game
    def stop (self):
        self.running = False
        print("game has stopped")

