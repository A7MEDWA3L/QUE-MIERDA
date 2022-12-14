import turtle
from turtle import*
def home():
    t.speed(5)
    t.penup()
    t.home()
    t.pendown()
    t.speed(3)

t=turtle
t.hideturtle()
t.title("NAZI")
t.bgcolor("red")
pencolor("white")
dot(325)
pencolor("black")
t.pensize(30)

t.left(135)
t.fd(100)
t.right(90)
t.fd(100)

home()
t.right(45)
t.fd(100)
t.right(90)
t.fd(100)

home()
t.left(225)
t.fd(100)
t.right(90)
t.fd(100)

home()
t.right(-45)
t.fd(100)
t.right(90)
t.fd(100)

exitonclick()