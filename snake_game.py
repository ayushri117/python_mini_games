import turtle
import time
import random



delay=0.1
score=0
high_score=0


wn=turtle.Screen()
wn.title("Snake Game By Ayush")
wn.bgcolor("yellow")
wn.setup(width=700,height=700)
wn.tracer(0)


head=turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("black")
head.penup()
head.goto(0,0)
head.direction='stop'

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(100,100)

body=[]

sc=turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("grey")
sc.penup()
sc.hideturtle()
sc.goto(0,300)
sc.write(f"Score:0 High Score: {high_score}",align="center",font=("ds-digital",25,"underline"))




def go_up():
    head.direction="up"

def go_down():
    head.direction="down"

def go_left():
    head.direction="left"

def go_right():
    head.direction="right"


def move():
    if head.direction =="down":
        y=head.ycor()
        head.sety(y-20)

    if head.direction =="up":
        y=head.ycor()
        head.sety(y+20)


    if head.direction =="right":
        x=head.xcor()
        head.setx(x+20)


    if head.direction =="left":
        x=head.xcor()
        head.setx(x-20)


wn.listen()
wn.onkeypress(go_up,"Up")
wn.onkeypress(go_down,"Down")
wn.onkeypress(go_right,"Right")
wn.onkeypress(go_left,"Left")



while True:
    wn.update()

    if head.xcor()>340 or head.xcor()<-340 or head.ycor()<-340 or head.ycor()>340:
        time.sleep(1)
        head.goto(0,0)
        head.direction="stop"
        for segment in body:
            segment.goto(2000,2000)
        body.clear()
        score=0
        delay=0.1
        sc.clear()
        sc.write(f"Score:{score} High Score: {high_score}",align="center",font=("ds-digital",25,"underline"))


    if head.distance(food)<20:
        food.goto(random.randint(-335,335),random.randint(-335,290))
        new_seg=turtle.Turtle()
        new_seg.speed(0)
        new_seg.shape("square")
        new_seg.color("grey")
        new_seg.penup()
        body.append(new_seg)

        delay-=0.003
        score+=5
        if score> high_score:
            high_score=score

        sc.clear()
        sc.write(f"Score:{score} High Score: {high_score}",align="center",font=("ds-digital",25,"underline"))

    for i in range(len(body)-1,0,-1):
        body[i].goto(body[i-1].xcor(),body[i-1].ycor())

    if len(body)>0:
        body[0].goto(head.xcor(),head.ycor())
    move()

    for segment in body:
        if segment.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            for segment in body:
                segment.goto(2000,2000)
            body.clear()
            score=0
            delay=0.1
            sc.clear()
            sc.write(f"Score:{score} High Score: {high_score}",align="center",font=("ds-digital",25,"normal"))
    time.sleep(delay)
    
wn.mainloop()