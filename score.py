from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 46, 'bold')


class Score(Turtle):
    def __init__(self, player1, player2):
        super().__init__()
        self.player_1_Score = 0
        self.player_2_Score = 0
        self.color('white')
        self.penup()
        self.goto(x=0, y=230)
        self.partition()
        self.update_score(player1=player1, player2=player2)
        self.hideturtle()

    def partition(self):
        self.penup()
        self.goto(x=0, y=300)
        self.right(90)
        self.speed('fastest')
        for i in range(30):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

    def update_score(self, player1, player2):
        self.partition()
        self.goto(0, 230)
        self.write(arg=f"{player1}: {self.player_1_Score}   {player2}: {self.player_2_Score}",
                   align=ALIGNMENT, font=FONT)

    def increase_p1_score(self, player1, player2):
        self.player_1_Score += 1
        self.clear()
        self.update_score(player1, player2)
        self.partition()

    def increase_p2_score(self, player1, player2):
        self.player_2_Score += 1
        self.clear()
        self.update_score(player1, player2)
        self.partition()

    def player_wins(self, winner):
        self.clear()
        self.goto(0, 0)
        self.write(arg=f"{winner} Wins", align=ALIGNMENT, font=FONT)
