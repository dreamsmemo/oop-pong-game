from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)

    def move_up(self):
        move_up_ycor = self.ycor() + 30
        self.goto(self.xcor(), move_up_ycor)

    def move_down(self):
        move_down_ycor = self.ycor() - 30
        self.goto(self.xcor(), move_down_ycor)





