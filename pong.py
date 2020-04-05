#Basic Pong Game
import turtle
import winsound

#Creates window
wn = turtle.Screen()
#Adds window title
wn.title("Game of Pong")
#Changes background color
wn.bgcolor("black")
#Sets window size
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_a = 0
score_b = 0

#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=3, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(+350, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.3
ball.dy = -0.3

#Pen Message on Screen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0 - Player B: 0", align="center", font=("Unispace", 24, "normal"))


#Function
#Paddle A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 40
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y += -40
    paddle_a.sety(y)

#Paddle B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 40
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y += -40
    paddle_b.sety(y)

#Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

#Main Game Loop
while True:
    wn.update()

    #Moves ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border Check
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -0.5
        winsound.PlaySound('C:/Users/ianha/OneDrive/Desktop/Play Store Project/pong/boing.wav', winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -0.5
        winsound.PlaySound('C:/Users/ianha/OneDrive/Desktop/Play Store Project/pong/boing.wav', winsound.SND_ASYNC)        

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= 1
        score_a += 1
        pen.clear()
        pen.write("Player A: {} - Player B: {}".format(score_a, score_b), align="center", font=("Unispace", 24, "normal"))
    
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= 1   
        score_b += 1
        pen.clear()
        pen.write("Player A: {} - Player B: {}".format(score_a, score_b), align="center", font=("Unispace", 24, "normal"))

    #Paddle and Ball Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound('C:/Users/ianha/OneDrive/Desktop/Play Store Project/pong/boing.wav', winsound.SND_ASYNC)

    if (ball.xcor() < -340 and ball.xcor() < -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound('C:/Users/ianha/OneDrive/Desktop/Play Store Project/pong/boing.wav', winsound.SND_ASYNC)