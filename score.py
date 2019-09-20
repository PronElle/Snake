from config import *


class UpperItem(turtle.Turtle):
    def __init__(self, pos, img, img_pos):
        turtle.Turtle.__init__(self)
        self.speed(0)
        self.color('Black')
        self.penup()
        self.setposition(pos)
        self.value = 0
        self.logo = self.create_logo(img, img_pos)

    def display(self):
        self.write(self.value, False, align='left', font=('Arial', 14, 'normal'))
        self.hideturtle()

    @staticmethod
    def create_logo(img, img_pos):
        logo = turtle.Turtle()
        logo.shape(img)
        logo.speed(0)
        logo.penup()
        logo.goto(img_pos)
        return logo


class Score(UpperItem):
    def __init__(self):
        UpperItem.__init__(self, SCORE_POS, APPLE_PATH, APPLE_LOGO_POS)

    def update(self):
        self.value += 1
        self.clear()

    def reset(self):
        self.value = 0
        self.clear()


class Record(UpperItem):
    def __init__(self):
        UpperItem.__init__(self, RECORD_POS, TROPHY_PATH, TROPHY_LOGO_POS)

    def update(self, current):
        self.value = max(self.value, current)
        self.clear()
