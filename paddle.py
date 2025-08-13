import turtle

width_rectangle = 20
height_rectangle = 100
rectangle = (
    (-width_rectangle/2, -height_rectangle/2),
    ( width_rectangle/2, -height_rectangle/2),
    ( width_rectangle/2,  height_rectangle/2),
    (-width_rectangle/2,  height_rectangle/2)
)

X_COOR_PLAYER1 = 350
X_COOR_PLAYER2 = -350
Y_COOR_PLAYER1 = 0
Y_COOR_PLAYER2 = 0

turtle.register_shape('my_rectangle', rectangle)


class Paddle(turtle.Turtle):
    def __init__(self, color, player_number):
        super().__init__()
        self.setheading(90)
        self.penup()
        self.shape('my_rectangle')
        self.color(color)
        if player_number == 1:
            self.goto(X_COOR_PLAYER1, Y_COOR_PLAYER1)
        elif player_number == 2:
            self.goto(X_COOR_PLAYER2, Y_COOR_PLAYER2)
        else:
            raise Exception('Paddle ID is not allowed (only Player 1 or Player 2)')


    def move_paddle_up(self):
        if self.ycor() < 240:
            self.sety(self.ycor() + 20)

    def move_paddle_down(self):
         if self.ycor() > -240:
            self.sety(self.ycor() - 20)
