from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 80, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score_1 = 0
        self.score_2 = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.update_scoreboard()


    def point_1 (self):
        self.score_1 += 1
        print(f"{self.score_1} es la puntuacion del jugador 1")
    def point_2 (self):
        self.score_2 += 1
        print(f"{self.score_2} es la puntuacion del jugador 2")


    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.score_1, False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write( self.score_2, False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= ALIGNMENT, font = FONT)



