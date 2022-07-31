import time
from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard

# Constants
FONT = ('Arial', 20, 'bold')

# Screen Set Up
pong_screen = Screen()
pong_screen.setup(800, 600)
pong_screen.bgcolor("black")
pong_screen.title("Pong Game")
pong_screen.tracer(0)

# Ball Set Up
ball = Ball()

# Paddle Set Up
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

# Score Set Up
score = ScoreBoard()

pong_screen.listen()
pong_screen.onkeypress(r_paddle.move_up, "Up")
pong_screen.onkeypress(r_paddle.move_down, "Down")
pong_screen.onkeypress(l_paddle.move_up, "w")
pong_screen.onkeypress(l_paddle.move_down, "s")

is_game_on = True

while is_game_on:
    time.sleep(0.04)
    pong_screen.update()
    ball.ball_move()

    # Detect collision with top and bottom wall
    if ball.ycor() == 290 or ball.ycor() == -290:
        ball.bounce_on_wall()

    # Detect collision with right paddle
    if ball.distance(r_paddle) < 20 or \
            (ball.xcor() > 360 and ball.distance(r_paddle) < 50):
        ball.bounce_on_paddle()
        score.update_r_score()

    # Detect collision with left paddle
    elif ball.distance(l_paddle) < 20 or \
            (ball.xcor() < -360 and ball.distance(l_paddle) < 50):
        ball.bounce_on_paddle()
        score.update_l_score()

    # if R player misses the ball
    if ball.xcor() > 380:
        ball.switch_side()
        score.update_l_score()

    # if L player misses the ball
    if ball.xcor() < -380:
        ball.switch_side()
        score.update_r_score()

pong_screen.exitonclick()
