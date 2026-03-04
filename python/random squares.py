import turtle
import random

t = turtle.Turtle()
for i in range(50):
    '''t.speed(0)'''
    angle = random.randint(0, 90)
    sqrlen = random.randint(10, 100)
    uplefcor = [random.randint(-200, 200), random.randint(-200, 200)]
    t.penup()
    t.goto(uplefcor[0], uplefcor[1])
    t.pendown()
   
    for j in range(4):
        t.forward(sqrlen)
        t.right(90)

    
turtle.done()