from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("white")
        self.penup()
        self.goto(position)
        self.setheading(90)

    def move(self):

        self.forward(20)

    def up(self):
        if self.heading() == 90:
            self.move()
        else:
            self.setheading(90)
            self.move()

    def down(self):
        if self.heading() != 90:
            self.move()
        else:
            self.setheading(270)
            self.move()
