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

player_paddle_dy = 0

def player_up():
    global player_paddle_dy
    player_paddle_dy = 1.5  # 이동 속도 설정

def player_down():
    global player_paddle_dy
    player_paddle_dy = -1.5  # 이동 속도 설정

def stop_player():
    global player_paddle_dy
    player_paddle_dy = 0  # 이동 멈춤
    
win.update()
win.mainloop()