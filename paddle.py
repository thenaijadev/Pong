from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(x, y)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.x, new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.x, new_y)
