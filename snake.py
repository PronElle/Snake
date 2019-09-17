import turtle
from vars import *


class Snake:
    def __init__(self):
        self.head = Head()
        self.queue = list()

    def add_piece(self):
        self.queue.append(Piece())

    def up(self):
        self.head.direction = Direction.UP

    def down(self):
        self.head.direction = Direction.DOWN

    def left(self):
        self.head.direction = Direction.LEFT

    def right(self):
        self.head.direction = Direction.RIGHT

    def move(self):
        for i in range(len(self.queue) - 1, 0, -1):  # pieces shifting
            self.queue[i].goto(self.queue[i - 1].xcor(), self.queue[i - 1].ycor())

        if len(self.queue) > 0:
            self.queue[0].goto(self.head.xcor(), self.head.ycor())

        if self.head.direction == Direction.UP:
            self.head.sety(self.head.ycor() + STEP)

        elif self.head.direction == Direction.DOWN:
            self.head.sety(self.head.ycor() - STEP)

        elif self.head.direction == Direction.LEFT:
            self.head.setx(self.head.xcor() - STEP)

        elif self.head.direction == Direction.RIGHT:
            self.head.setx(self.head.xcor() + STEP)


class Piece(turtle.Turtle):
    def __init__(self, color="Grey"):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color(color)
        self.speed(0)
        self.penup()


class Head(Piece):
    def __init__(self):
        Piece.__init__(self, "Black")
        self.goto(-30, 30)
        self.direction = Direction.STOP
