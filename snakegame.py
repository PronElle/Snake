from time import sleep
from snake import Snake
from food import Food
from config import *
from tkinter import messagebox
from score import Score, Record


class SnakeGame:
    def __init__(self, grid_size, step):
        self.snake = Snake()
        self.food = Food()
        self.score = Score()
        self.record = Record()
        self.board = turtle.Screen()

        self.board.title('Snake')
        self.board.bgpic(BG_PATH)
        self.board.bgcolor('Green')
        self.board.setup(width=SCREEN, height=SCREEN)
        self.board.tracer(0)
        self.grid = self.grid_builder(grid_size, step)
        self.delay = DELAY

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
        self.board.onkey(self.snake.up, 'Up')
        self.board.onkey(self.snake.down, 'Down')
        self.board.onkey(self.snake.right, 'Right')
        self.board.onkey(self.snake.left, 'Left')
        self.board.onkey(self.pause, 'p')    # secret command
        self.board.onkey(self.restart, 'r')  # secret command

    def pause(self):
        self.snake.head.direction = Direction.STOP

    def restart(self):
        self.score.reset()
        for q in self.snake.queue:
            q.hideturtle()
        self.snake.queue.clear()

        self.snake.head.goto(SNAKE_START)
        self.snake.head.direction = Direction.STOP
        self.food.goto(FOOD_START)
        self.delay = DELAY

    def play_again(self):
        msg_box = messagebox.askquestion('GAME OVER',
                                         'Score:\t{}\n'
                                         'Best: \t{}\n'
                                         'Wanna play again?'
                                         .format(self.score.value, self.record.value))
        if msg_box == 'yes':
            self.restart()
            return True
        else:
            return False

    def game_over(self):
        return self.snake.head.xcor() > BORD \
               or self.snake.head.xcor() < -BORD \
               or self.snake.head.ycor() > BORD \
               or self.snake.head.ycor() < - BORD \
               or any(piece.distance(self.snake.head) < 10 for piece in self.snake.queue)

    def gameplay(self):
        game_on = True
        while game_on:
            while not self.game_over():
                self.score.display()
                self.record.display()
                self.commands()

                if self.snake.head.distance(self.food) < STEP:
                    self.food.reposition()
                    self.snake.add_piece()
                    self.delay -= 0.001
                    self.score.update()
                    self.record.update(self.score.value)

                self.snake.move()
                sleep(self.delay)

                self.board.update()

            game_on = self.play_again()


if __name__ == '__main__':
    game = SnakeGame(GRID, STEP)
    game.gameplay()
