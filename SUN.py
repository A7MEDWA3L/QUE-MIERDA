from turtle import *
hideturtle()
speed(10)
pensize(1)
bgcolor('black')
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()