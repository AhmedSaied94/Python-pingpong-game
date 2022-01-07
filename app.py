#!/bin/env python3

import turtle #import tutle module
#screen
wind = turtle.Screen()  #create screen window
wind.title("PING PONG") #create name for the window
wind.bgcolor("black")    #setup color to the background
wind.tracer(0)   #stop screen from automataclly update
wind.setup(width=800, height=600)   #set up screen resuliotion

#madrab1
madrab1 = turtle.Turtle() #create madrab
madrab1.shape("square")   #select the shape of it
madrab1.shapesize(stretch_wid=5, stretch_len=1)   #setup madrab size
madrab1.color("green")   #select madrab color
madrab1.speed(0)         #select madrab speed
madrab1.penup()          #disable madrab from drawing lines when move
madrab1.goto(-370, 0)     #select where to be 

#madrab2
madrab2 = turtle.Turtle() #create madrab
madrab2.shape("square")   #select the shape of it
madrab2.shapesize(stretch_wid=5, stretch_len=1)   #setup madrab size
madrab2.color("yellow")   #select madrab color
madrab2.speed(0)         #select madrab speed
madrab2.penup()      #disable madrab from drawing lines when move
madrab2.goto(370, 0)     #select where to be 

#ball
ball = turtle.Turtle() #create ball
ball.shape("square")   #select the shape of it
ball.color("white")   #select ball color
ball.speed(1)         #select ball speed
ball.penup()          #disable ball from drawing lines when move
ball.goto(0, 0)     #select where to be 
ball.dx = 0.65
ball.dy = 0.65
#scores
score1 = 0
score2 = 0
score = turtle.Turtle()
score.speed(0)
score.penup()
score.hideturtle()
score.goto(0, 260)
score.color("white")
score.write("player1 : 0  player2 : 0", align="center", font=("arial",22,"bold"))
#functionss
def madrab1_up():
    y = madrab1.ycor()
    y += 30
    madrab1.sety(y)
def madrab2_up():
    y = madrab2.ycor()
    y += 30
    madrab2.sety(y)    
def madrab1_down():
    y = madrab1.ycor()
    y -= 30
    madrab1.sety(y)  
def madrab2_down():
    y = madrab2.ycor()
    y -= 30
    madrab2.sety(y)        
#keypad bulding
wind.listen()
wind.onkeypress(madrab1_up, "w") 
wind.onkeypress(madrab2_up, "Up") 
wind.onkeypress(madrab1_down, "s") 
wind.onkeypress(madrab2_down, "Down") 

 

#main loop
while True:
    wind.update()
# ball movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    if ball.xcor() > 390:
       ball.goto(0, 0)
       ball.dx *=-1
       score1 += 1
       score.clear()
       score.write("player1 : {}  player2 : {}".format(score1, score2), align="center", font=("arial",22,"bold"))
    if ball.ycor() < -290:
       ball.sety(-290)
       ball.dy *= -1 
    if ball.xcor() < -390:
       ball.goto(0, 0)
       ball.dx *= -1   
       score2 += 1
       score.clear()
       score.write("player1 : {}  player2 : {}".format(score1, score2), align="center", font=("arial",22,"bold"))
    if ball.xcor() > 360 and ball.xcor() < 370 and ball.ycor() < madrab2.ycor() +40 and ball.ycor() > madrab2.ycor() -40:
        ball.setx(360)
        ball.dx *= -1
    if ball.xcor() < -360 and ball.xcor() > -370 and ball.ycor() < madrab1.ycor() +40 and ball.ycor() > madrab1.ycor() -40:
        ball.setx(-360)
        ball.dx *= -1
 
