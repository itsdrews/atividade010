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


ball = Ball(x = randint(0, WINDOW_WIDTH), y = randint(200, WINDOW_HEIGHT), radius = BALL_RADIUS, color = BALL_COLOR)
left_wall = Walls(x = 10,y=0, width=10, height=WINDOW_HEIGHT)
right_wall = Walls(x = 700, y = 0, width=10, height=WINDOW_HEIGHT)
upper_wall = Walls(x = 0 , y = 0 ,width = WINDOW_WIDTH, height = 10)
paddle = Paddle(x = PADDLE_CENTER_X,y = PADDLE_CENTER_Y ,width = PADDLE_WIDTH,height = PADDLE_HEIGHT)
blocks = Blocks()
class Game:
    def __init__(self):
        self.running = False

    def start(self):
        self.running = True
        a = 0
        while self.running:
            print("game is running")
            a +=1
            if a==100:
                self.stop()

    def idle_screen(self):
        self.running = True
        while self.running:
            print("Idle Screen")



    def stop (self):
        self.running = False
        print("game has stopped")

