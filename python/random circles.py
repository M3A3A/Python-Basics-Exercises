import turtle
import random

t = turtle.Turtle()
for i in range (20):
    radii = [random.randint(5, 50)]
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    a = [x ,y]
    t.penup()
    t.goto(a[0], a[1])
    t.pendown() 
    t.circle(radii[0])
    
turtle.done()