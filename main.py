import turtle
import random
# 화면 설정
win = turtle.Screen()
win.title("Pong Game with AI")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)

# 패들(왼쪽: 플레이어)
player_paddle = turtle.Turtle()
player_paddle.speed(0)
player_paddle.shape("square")
player_paddle.color("white")
player_paddle.shapesize(stretch_wid=6, stretch_len=1)
player_paddle.penup()
player_paddle.goto(-350, 0)

# 패들(오른쪽: AI)
ai_paddle = turtle.Turtle()
ai_paddle.speed(0)
ai_paddle.shape("square")
ai_paddle.color("red")
ai_paddle.shapesize(stretch_wid=6, stretch_len=1)
ai_paddle.penup()
ai_paddle.goto(350, 0)

# 공
ball = turtle.Turtle()
ball.speed(40)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # 공의 x 속도
ball.dy = 0.2  # 공의 y 속도

# 점수판
score_a = 0
score_b = 0

score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write(f"Player: {score_a}  AI: {score_b}", align="center", font=("Courier", 24, "normal"))

# 점수 업데이트 함수
def update_score():
    score_display.clear()
    score_display.write(f"Player: {score_a}  AI: {score_b}", align="center", font=("Courier", 24, "normal"))



win.update()
win.mainloop()