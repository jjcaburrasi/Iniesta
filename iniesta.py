import turtle
import time
import random
import keyboard
from collections import deque
from io import open

archivo=open("archivo.txt", "r")
delay = 0.1
score = 0
high_score = 0

 
 
 
# Creating a window screen
wn = turtle.Screen()
wn.title("Andres Iniesta: Midfielder")
wn.bgcolor("green")
# the width and height can be put as user's choice
wn.setup(width=1000, height=600)
wn.tracer(0)
#Creo circulo central
centro= turtle.Turtle ()
centro.penup()
centro.goto(0, -175)
centro.pendown()
centro.pensize(10)
centro.pencolor("white")
centro.circle(175)
centro.penup()
centro.hideturtle()
#Creando linea central
linea=turtle.Turtle()
linea.pensize(10)
linea.pencolor("white")
linea.goto(0,300)
linea.goto(0,-300)
linea.hideturtle()
linea.goto(0,200)
linea.goto(490,300)
linea.goto(490,-300)
linea.goto(-490,-300)
linea.goto(-490,300)
linea.goto(0,300)
linea.hideturtle()

# iniesta
iniesta = turtle.Turtle()
iniesta.shape("circle")
iniesta.color("white")
iniesta.penup()
iniesta.goto(-50, 0)
iniesta.direction = "Stop"
#defensa1
defensa = turtle.Turtle()
posiciondefensay= random.randint(-290,290)
defensa.shape("circle")
defensa.color("blue")
defensa.penup()
defensa.goto(490,posiciondefensay)
defensa.direction = "left"
#defensa2
defensa2 = turtle.Turtle()
posiciondefensay= random.randint(-290,290)
defensa2.shape("circle")
defensa2.color("blue")
defensa2.penup()
defensa2.goto(490,posiciondefensay)
defensa2.direction = "left"
#defensa3
defensa3 = turtle.Turtle()
posiciondefensay= random.randint(-290,290)
defensa3.shape("circle")
defensa3.color("blue")
defensa3.penup()
defensa3.goto(490,posiciondefensay)
defensa3.direction = "left"
 
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(250, 250)
pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(-250, 250)
pen2.write("Andrés Iniesta: Midfielder".format(), align="center", font=("candara", 24, "bold"))





# assigning key directions
def goup():
    teclas_almacenadas.extend("w")
    if iniesta.direction != "down":
        iniesta.direction = "up"
def godown():
    teclas_almacenadas.extend("s")
    if iniesta.direction != "up":
        iniesta.direction = "down"


        iniesta.direction = "down" 
def goleft():
    teclas_almacenadas.extend("a")
    if iniesta.direction != "right":
        iniesta.direction = "left"
def goright():
    teclas_almacenadas.extend("d")
    if iniesta.direction != "left":
        iniesta.direction = "right"


        iniesta.direction = "right" 
def move():
    if iniesta.direction == "up":
        y = iniesta.ycor()
        iniesta.sety(y+20)
    if iniesta.direction == "down":
        y = iniesta.ycor()
        iniesta.sety(y-20)
    if iniesta.direction == "left":
        x = iniesta.xcor()
        iniesta.setx(x-20)
    if iniesta.direction == "right":
        x = iniesta.xcor()
        iniesta.setx(x+20)
def movedefensa():
    if defensa.direction == "up":
        y = defensa.ycor()
        defensa.sety(y+1)
    if defensa.direction == "down":
        y = defensa.ycor()
        defensa.sety(y-10)
    if defensa.direction == "left":
        x = defensa.xcor()
        defensa.setx(x-10)
    if defensa.direction == "right":
        x = defensa.xcor()
        defensa.setx(x+10)
def movedefensa2():
    if defensa2.direction == "up":
        y = defensa2.ycor()
        defensa2.sety(y+1)
    if defensa2.direction == "down":
        y = defensa2.ycor()
        defensa2.sety(y-10)
    if defensa2.direction == "left":
        x = defensa2.xcor()
        defensa2.setx(x-10)
    if defensa2.direction == "right":
        x = defensa2.xcor()
        defensa2.setx(x+10)
def movedefensa3():
    if defensa3.direction == "up":
        y = defensa3.ycor()
        defensa3.sety(y+1)
    if defensa3.direction == "down":
        y = defensa3.ycor()
        defensa3.sety(y-10)
    if defensa3.direction == "left":
        x = defensa3.xcor()
        defensa3.setx(x-10)
    if defensa3.direction == "right":
        x = defensa3.xcor()
        defensa3.setx(x+10)
def easteregg():
    wn.bgcolor("green")
    pen3 = turtle.Turtle()
    pen3.speed(0)
    pen3.color("white")
    pen3.penup()
    pen3.hideturtle()
    pen3.goto(0,-220)
    pen3.write("Juego desarrollado por Jose Caburrasi".format(), align="center", font=("candara", 24, "bold"))

#Easteregg
easter_egg_trigger = "wwssadad"
teclas_almacenadas = deque([], len(easter_egg_trigger))

wn.listen()
wn.onkeypress(goup, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []
while True:

#salir por un lado y entrar por el otro
    wn.update()
    if "".join(teclas_almacenadas) == easter_egg_trigger:
      easteregg()
    if iniesta.xcor() > 490 or iniesta.xcor() < -490 or iniesta.ycor() > 290 or iniesta.ycor() < -290:
        if score > high_score:
            high_score = score
        time.sleep(1)
        iniesta.goto(-50, 0)
        iniesta.direction = "Stop"
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        iniesta.goto(-50, 0)
        iniesta.direction = "Stop"
    if defensa.xcor()<-500:
        defensa.hideturtle()
        defensa = turtle.Turtle()
        posiciondefensay= random.randint(-290,290)
        defensa.shape("circle")
        defensa.color("blue")
        defensa.penup()
        defensa.goto(490,posiciondefensay)
        defensa.direction = "left"
        score+=1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if defensa.distance(iniesta)<27:
        if score > high_score:
            high_score = score
        time.sleep(1)
        iniesta.goto(-50, 0)
        iniesta.direction = "Stop"
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    if defensa2.xcor()<-500:
        defensa2.hideturtle()
        defensa2 = turtle.Turtle()
        posiciondefensay= random.randint(-290,290)
        defensa2.shape("circle")
        defensa2.color("blue")
        defensa2.penup()
        defensa2.goto(490,posiciondefensay)
        defensa2.direction = "left"
        score+=1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    if defensa2.distance(iniesta)<25:
        if score > high_score:
            high_score = score
        time.sleep(1)
        iniesta.goto(-50, 0)
        iniesta.direction = "Stop"
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        
    if defensa3.xcor()<-500:
        defensa3.hideturtle()
        defensa3 = turtle.Turtle()
        posiciondefensay= random.randint(-290,290)
        defensa3.shape("circle")
        defensa3.color("blue")
        defensa3.penup()
        defensa3.goto(490,posiciondefensay)
        defensa3.direction = "left"
        score+=1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
    if defensa3.distance(iniesta)<25:
        if score > high_score:
            high_score = score
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(score, high_score), align="center", font=("candara", 24, "bold"))
        time.sleep(1)
        iniesta.goto(-50, 0)
        iniesta.direction = "Stop"
           

    move()
    movedefensa()
    movedefensa()
    movedefensa()
    movedefensa()
    movedefensa()
    movedefensa()
    movedefensa2()
    movedefensa2()
    movedefensa2()
    movedefensa2()
    movedefensa2()
    movedefensa3()
    movedefensa3()
    movedefensa3()


    time.sleep(delay)



wn.mainloop()




