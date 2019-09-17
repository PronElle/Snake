import turtle
from time import sleep
from snake import Snake
from food import Food
from vars import *


class SnakeGame:
    def __init__(self, grid_size, step):
        self.snake = Snake()
        self.food = Food()
        self.board = turtle.Screen()
        self.board.title("Snake")
        self.board.bgcolor("Green")
        self.board.setup(width=grid_size, height=grid_size)
        self.board.tracer(0)
        self.grid = self.grid_builder(grid_size, step)
        self.delay = 0.12
        self.pause = False

    @staticmethod
    def grid_builder(grid_size, step):
        grid = turtle.Turtle()
        grid.ht()
        for x in range(- grid_size // 2 // step, grid_size // 2 // step):
            for y in range(- grid_size // 2 // step, grid_size // 2 // step):
                grid.up()
                grid.goto(x * step, y * step)
                grid.down()
                for sizes in range(4):
                    grid.forward(step)
                    grid.left(90)
        return grid

    def commands(self):
        self.board.listen()
        self.board.onkey(self.snake.up, "Up")
        self.board.onkey(self.snake.down, "Down")
        self.board.onkey(self.snake.right, "Right")
        self.board.onkey(self.snake.left, "Left")
        self.board.onkey(self.start_stop, "p")

    def start_stop(self):
        self.pause = not self.pause

    def game_over(self):
        return self.snake.head.xcor() > BORD \
               or self.snake.head.xcor() < -BORD \
               or self.snake.head.ycor() > BORD \
               or self.snake.head.ycor() < - BORD \
               or any(piece.distance(self.snake.head) < 10 for piece in self.snake.queue)

    def gameplay(self):
        while not self.game_over():
            if not self.pause:
                self.commands()

                if self.snake.head.distance(self.food) < STEP:
                    self.food.reposition()
                    self.snake.add_piece()
                    self.delay -= 0.001

                self.snake.move()
                sleep(self.delay)

            self.board.update()

        turtle.write("GAME OVER!", font=('Verdana', 40, 'normal'), align="center")
        turtle.hideturtle()


if __name__ == '__main__':
    game = SnakeGame(GRID, STEP)
    game.gameplay()
    game.board.exitonclick()

