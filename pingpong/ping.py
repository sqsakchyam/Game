import turtle

wind = turtle.Screen()
wind.title("Ping Pong")
wind.bgcolor("black")
wind.setup(width=800, height=600)
wind.tracer(0)

#Track Score
score_a = 0
score_b = 0

#Side bar thing
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.color("white")
bar_a.shapesize(stretch_wid=5,stretch_len=1)
bar_a.penup()
bar_a.goto(-350,0)

bar_b = turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.color("white")
bar_b.shapesize(stretch_wid=5,stretch_len=1)
bar_b.penup()
bar_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.2
ball.dy = -0.2

#Score
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player A:0 Player B:0", align="center", font=("Courier", 24, "normal"))
#Function
def bar_a_up():
    y = bar_a.ycor()
    y += 40
    bar_a.sety(y)

def bar_a_down():
    y = bar_a.ycor()
    y -= 40
    bar_a.sety(y)

def bar_b_up():
    y = bar_b.ycor()
    y += 40
    bar_b.sety(y)

def bar_b_down():
    y = bar_b.ycor()
    y -= 40
    bar_b.sety(y)

#keyboard Movement
wind.listen()
wind.onkeypress(bar_a_up,"w")
wind.onkeypress(bar_a_down,"s")
wind.onkeypress(bar_b_up,"Up")
wind.onkeypress(bar_b_down,"Down")


#Game loop
while True:
    wind.update()

    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *=-1
        score_a +=1
        score.clear()
        score.write("Player A:{} Player B:{}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score.clear()
        score.write("Player A:{} Player B:{}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    #bar and ball collison
    if (ball.xcor() > 340 and ball.xcor() <350) and (ball.ycor() < bar_b.ycor() + 40 and ball.ycor() > bar_b.ycor() - 40):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bar_a.ycor() + 40 and ball.ycor() > bar_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *=-1



