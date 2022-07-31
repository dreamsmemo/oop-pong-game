from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.goto(0, 0)
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def ball_move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move
        self.goto(new_x_cor, new_y_cor)

    def bounce_on_wall(self):
        self.y_move *= -1

    def bounce_on_paddle(self):
        self.x_move *= -1
        self.move_speed *= 0.7

    def switch_side(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
