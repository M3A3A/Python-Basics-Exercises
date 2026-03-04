import turtle

lis = []
for i in range (10):
    print("Enter the coordinates of point", i+1)
    x = int(input("x: "))
    y = int(input("y: "))
    lis.append([x,y])
t = turtle.Turtle()
for i in range (10):
    t.penup()
    t.goto(lis[i][0],lis[i][1])
    t.dot(2,"red")

for i in  range (10):
    t.pendown()
    t.goto(lis[i][0],lis[i][1])


turtle.done()
