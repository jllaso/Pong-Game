import time
from turtle import Turtle
import math

SPEED_BALL = [300, 500, 700]
ANGLE_BALL = 60
PADDLE_HALF_HEIGHT = 50

class Ball(Turtle):
    def __init__(self, difficulty_level):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0,0)

        # velocity components (px/s), computed on launch
        if difficulty_level.lower() == 'easy':
            self._speed_px_s = SPEED_BALL[0]
        elif difficulty_level.lower() == 'medium':
            self._speed_px_s = SPEED_BALL[1]
        elif difficulty_level.lower() == 'hard':
            self._speed_px_s = SPEED_BALL[2]
        self._angle_rad = math.radians(ANGLE_BALL)
        self.vx = 0.0
        self.vy = 0.0


    def move(self, dt):
        # dt = seconds since last frame
        self.setx(self.xcor() + self.vx * dt)
        self.sety(self.ycor() + self.vy * dt)

    def launch(self, orientation):
        # set velocity toward top-right
        self.vx = orientation*self._speed_px_s * math.cos(self._angle_rad)
        self.vy = orientation*self._speed_px_s * math.sin(self._angle_rad)

    def wall_bounce(self):
         self.vy = -self.vy

    def paddle_bounce(self, paddle):
        self.vx = -self.vx

        # Distance from paddle center to ball
        offset = self.ycor() - paddle.ycor()

        # paddle is 100 px tall → half = 50
        paddle_half_height = PADDLE_HALF_HEIGHT
        normalized = max(-1.0, min(1.0, offset / PADDLE_HALF_HEIGHT))  # clamp [-1, 1]

        # max deflection angle from horizontal (tweakable)
        max_angle = math.radians(45)
        bounce_angle = normalized * max_angle

        # keep total speed constant
        speed = math.hypot(self.vx, self.vy)

        # rebuild velocity from angle; sign of vx already flipped above
        self.vx = math.copysign(speed * math.cos(bounce_angle), self.vx)
        self.vy = speed * math.sin(bounce_angle)

        # nudge the ball just outside the paddle to avoid double-bounce
        if self.vx > 0:  # heading right after bounce
            self.setx(paddle.xcor() + 20)  # 20 ~ half ball diameter + a bit
        else:  # heading left
            self.setx(paddle.xcor() - 20)


    def out_of_bounds(self, player):
        self.goto(0,0)
        self.vx = 0
        self.vy = 0
        time.sleep(1)
        if player == 1:
            self.launch(-1)
        if player == 2:
            self.launch(1)

