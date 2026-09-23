from turtle import Turtle , Screen
from ball import Ball
from paddle import Paddle 
from score import Scoreboard
import time
screen = Screen()
screen.title("Ping pong game")
screen.bgcolor("black")
screen.setup(800,600) 
screen.tracer(0)
ball = Ball()
scoreboard = Scoreboard()
player_paddle = Paddle((0,-250))
screen.listen()
screen.onkey(player_paddle.go_left,"Left")
screen.onkey(player_paddle.go_right,"Right")
shape_speed = 0.1
game_on = True
while game_on:
    screen.update()
    time.sleep(shape_speed)
    ball.move()
    if ball.distance(player_paddle) < 50 and ball.ycor() < -230 :
        shape_type = ball.shape()
        shape_color = ball.color()[0]
        if shape_type == "turtle":
            if shape_color == "white":
               game_on = False
               scoreboard.game_over()
            else:
               prints = 5
               scoreboard.increase_score(points)
        elif shape_type == "circle":
               points = 1
               scoreboard.increase_score(points)
        elif shape_type == "square":
               points = 2
               scoreboard.increase_score(points)
        elif shape_type == "triangle":
               scoreboard.reset_score()
        ball.reset_position()
        shape_speed*=0.9
    if ball.ycor() < -300:
         ball.reset_position()
   
screen.exitonclick()