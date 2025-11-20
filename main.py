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

def reset_game():
    global game_over
    ball.goto(0, 0)
    ball.dx = 0.2
    ball.dy = 0.2
    game_over = False
    score_display.clear()
    score_display.goto(0, 260)
    score_display.write(f"Player: {score_a}  AI: {score_b}", align="center", font=("Courier", 24, "normal"))

def reset_score():
    global score_a, score_b
    score_a = 0
    score_b = 0
    update_score()


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

# 키 입력 설정
win.listen()
win.onkeypress(player_up, "Up")
win.onkeypress(player_down, "Down")
win.onkeyrelease(stop_player, "Up")
win.onkeyrelease(stop_player, "Down")

#게임 루프
game_over = False

def check_game_over():
    global game_over
    if score_a >= 1 or score_b >= 1: 
        game_over = True
        score_display.clear()
        score_display.goto(0, 0)
        score_display.write(f"Player: {score_a}  AI: {score_b}", align="center", font=("Courier", 24, "normal"))
        score_display.goto(0, -30)
        score_display.write("Game Over! Press Space to Restart", align="center", font=("Courier", 24, "normal"))

while True:
    win.update()

    if game_over:
        continue
    player_paddle.sety(player_paddle.ycor() + player_paddle_dy)
    # 공 이동
    ball.setx(ball.xcor() + ball.dx * 5)
    ball.sety(ball.ycor() + ball.dy)
    ball.speed(50)

   # 벽 충돌 (위, 아래)
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # 방향 반전
        ball.dy += random.uniform(-0.1, 0.1)  # 랜덤한 y 속도 추가

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # 방향 반전
        ball.dy += random.uniform(-0.1, 0.1)  # 랜덤한 y 속도 추가 

    # 패들 충돌 (플레이어)
    if ball.xcor() < -340 and player_paddle.ycor() - 50 < ball.ycor() < player_paddle.ycor() + 50:
        ball.setx(-340)
        ball.dx *= -1
        # 공이 패들의 위쪽에 닿으면 위로, 아래쪽에 닿으면 아래로
        if ball.ycor() > player_paddle.ycor():
            ball.dy = abs(ball.dy)
        else:
            ball.dy = -abs(ball.dy)
        ball.dx *= 1.1  # 속도 증가
        ball.dy *= 1.1  # 속도 증가

    # AI 패들 움직임 (공 따라가기)
    if random.randint(0, 1) == 0:
        if ai_paddle.ycor() < ball.ycor() and abs(ai_paddle.ycor() - ball.ycor()) > 10:
            ai_paddle.sety(ai_paddle.ycor() + 0.5)  # 속도를 0.2에서 0.5로 증가
        elif ai_paddle.ycor() > ball.ycor() and abs(ai_paddle.ycor() - ball.ycor()) > 10:
            ai_paddle.sety(ai_paddle.ycor() - 0.5)  # 속도를 0.2에서 0.5로 증가
    if ai_paddle.ycor() < ball.ycor() and abs(ai_paddle.ycor() - ball.ycor()) > 10:
        ai_paddle.sety(ai_paddle.ycor() + 0.5)  # 속도를 0.2에서 0.5로 증가
    elif ai_paddle.ycor() > ball.ycor() and abs(ai_paddle.ycor() - ball.ycor()) > 10:
        ai_paddle.sety(ai_paddle.ycor() - 0.5)  # 속도를 0.2에서 0.5로 증가

       # 패들 충돌 (AI)
    if ball.xcor() > 340 and ai_paddle.ycor() - 50 < ball.ycor() < ai_paddle.ycor() + 50:
        ball.setx(340)
        ball.dx *= -1
        # 공이 패들의 위쪽에 닿으면 위로, 아래쪽에 닿으면 아래로
        if ball.ycor() > ai_paddle.ycor():
            ball.dy = abs(ball.dy)
        else:
            ball.dy = -abs(ball.dy)
        ball.dx *= 1.1  # 속도 증가
        ball.dy *= 1.1  # 속도 증가 

    # 공이 오른쪽 벽을 넘어가면 플레이어 점수 증가
    if ball.xcor() > 390:
        score_a += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1  # 반대 방향으로 재시작
        check_game_over()

    # 공이 왼쪽 벽을 넘어가면 AI 점수 증가
    if ball.xcor() < -390:
        score_b += 1
        update_score()
        ball.goto(0, 0)
        ball.dx *= -1  # 반대 방향으로 재시작
        check_game_over()
    
    