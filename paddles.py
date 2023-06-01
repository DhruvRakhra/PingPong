from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.left(90)
        self.color('yellow')
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)

    def move_up(self):
        if self.ycor() > 250:
            pass
        else:
            new_y = self.ycor() + 40
            self.goto(x=self.xcor(), y=new_y)

    def move_down(self):
        if self.ycor() < -250:
            pass
        else:
            new_y = self.ycor() - 40
            self.goto(x=self.xcor(), y=new_y)

    def reset_paddle(self, position):
        self.goto(position)
