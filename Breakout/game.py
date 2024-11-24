from ball import Ball
from walls import Walls
from score import Score
from blocks import Block
from paddle import Paddle
from random import randint
import keyboard
import time


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
BALL_SPEED = 5

#Blocks
yellow_blocks = []
green_blocks = []
orange_blocks = []
red_blocks = []



class Game:
    def __init__(self):
        self.running = False
        self.idle = True


    #draw all screen objects
    def create_screen_objects(self,ball : Ball,left_wall:Walls,right_wall:Walls,
                              uper_wall: Walls,paddle:Paddle):

        ball = Ball(x=randint(0, WINDOW_WIDTH), y=randint(210, WINDOW_HEIGHT-300), radius=BALL_RADIUS, color=BALL_COLOR,speed=BALL_SPEED)
        left_wall = Walls(x=100, y=0, width=10, height=WINDOW_HEIGHT)
        right_wall = Walls(x=700, y=0, width=10, height=WINDOW_HEIGHT)
        upper_wall = Walls(x=0, y=0, width=WINDOW_WIDTH, height=10)
        if self.idle == False:
            paddle = Paddle(center_x=PADDLE_CENTER_X, center_y=PADDLE_CENTER_Y, width=PADDLE_WIDTH, height=PADDLE_HEIGHT)
        else:
            paddle = Paddle(center_x=PADDLE_CENTER_X, center_y=PADDLE_CENTER_Y, width=WINDOW_WIDTH, height=PADDLE_HEIGHT)

        return [ball,left_wall,right_wall,upper_wall,paddle]

    #runs the game
    def start(self):
        self.running = True
        self.idle = False
        score = Score()
        screen = self.create_screen_objects(Ball, Walls, Walls, Walls, Paddle)
        ball = screen[0]
        left_wall = screen[1]
        right_wall = screen[2]
        upper_wall = screen[3]
        paddle = screen[4]
        yellow_blocks = self.create_blocks_row(200, 'yellow', Block)
        green_blocks = self.create_blocks_row(170, 'green', Block)
        orange_blocks = self.create_blocks_row(140, 'orange', Block)
        red_blocks = self.create_blocks_row(110, 'red', Block)

        ball_is_ghost = False
        print("game is running")
        while self.running:
            time.sleep(1)
            if score.max_score():
                print('WIN!!')
                self.stop()
                break


            paddle.handle_controls()
            paddle.check_max_min(left_wall,right_wall)
            ball.move()
            print(ball)
            print(score)
            print(paddle)
            ball.hit_wall(left_wall, right_wall, upper_wall,ball_is_ghost)
            ball.hit_paddle(paddle,ball_is_ghost)

            if self.check_hit(ball,yellow_blocks):
                ball_is_ghost= score.update_score('yellow')
                ball.toggle_ghost()

            if self.check_hit(ball,green_blocks):
                ball_is_ghost = score.update_score('green')
                ball.toggle_ghost()
            if self.check_hit(ball,orange_blocks):
                ball_is_ghost =score.update_score('orange')
                ball.toggle_ghost()
            if self.check_hit(ball,red_blocks):
                ball_is_ghost = score.update_score('red')
                ball.toggle_ghost()

            if keyboard.is_pressed('esc'):
                self.stop()






    #runs idle screen while not playing
    def idle_screen(self):
        screen = self.create_screen_objects(Ball,Walls,Walls,Walls,Paddle)
        ball = screen[0]
        left_wall = screen[1]
        right_wall = screen[2]
        upper_wall = screen[3]
        paddle = screen[4]
        yellow_blocks = self.create_blocks_row(200,'yellow',Block)
        green_blocks = self.create_blocks_row(170,'green',Block)
        orange_blocks = self.create_blocks_row(140,'orange',Block)
        red_blocks = self.create_blocks_row(110,'red',Block)




        self.running = True
        while self.running:
            ball.move()
            ball.hit_wall(left_wall, right_wall, upper_wall)
            ball.hit_paddle(paddle)

            if keyboard.is_pressed('esc'):
                self.stop()
                break
            elif keyboard.is_pressed('space'):
                self.start()
                break

    #closes the game
    def stop (self):
        self.running = False
        print("game has stopped")

    #creates the block rows
    def create_blocks_row(self,y,color,block:Block):
        block_rows =[]
        for i in range(14):
            block_down=Block(100 + i*5,y,color)
            block_rows.append(block_down)
            block_up= Block(100 + i*5,y-30,color)
            block_rows.append(block_up)

        return block_rows

    #check for scoring
    def check_hit(self, ball: Ball, block_list):
        if len(block_list) == 0:
            return
        else:
            for i in range(len(block_list)):
                check = ball.hit_block(block_list[i])
                if check:
                    ball.set_speed(block_list[i].color, ball.x_speed)
                    del block_list[i]
                    break








