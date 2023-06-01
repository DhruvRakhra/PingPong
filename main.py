from turtle import Screen
from paddles import Paddle
from ball import Ball
from score import Score
from time import sleep


my_screen = Screen()
my_screen.setup(width=800, height=600)
my_screen.title("My Pong Game")
my_screen.bgcolor("black")

player_1 = my_screen.textinput(title="Player Names", prompt="Enter Player 1's name: ")
player_2 = my_screen.textinput(title="Player Names", prompt="Enter Player 2's name")

my_screen.tracer(0)


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
score = Score(player1=player_1, player2=player_2)


my_screen.listen()
my_screen.onkey(key='w', fun=l_paddle.move_up)
my_screen.onkey(key='s', fun=l_paddle.move_down)
my_screen.onkey(key='Up', fun=r_paddle.move_up)
my_screen.onkey(key='Down', fun=r_paddle.move_down)

game_is_on = True

while game_is_on:
    sleep(ball.move_speed)
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.paddle_bounce()

    # right paddle misses
    if ball.xcor() > 390:
        score.increase_p1_score(player1=player_1, player2=player_2)
        ball.reset_position()
        l_paddle.reset_paddle((-350, 0))
        r_paddle.reset_paddle((350, 0))
        sleep(2)

    # left paddle misses
    if ball.xcor() < -390:
        score.increase_p2_score(player1=player_1, player2=player_2)
        ball.reset_position()
        l_paddle.reset_paddle((-350, 0))
        r_paddle.reset_paddle((350, 0))
        sleep(2)

    if score.player_1_Score >= 5:
        score.player_wins(player_1)
        game_is_on = False

    if score.player_2_Score >= 5:
        score.player_wins(player_2)
        game_is_on = False

    my_screen.update()


my_screen.exitonclick()
