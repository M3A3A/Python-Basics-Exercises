import turtle
lis = [["F",50],["L",90],["F",100],["R",90],["F",50]]
t = turtle.Turtle()

for i in range (len(lis)):
    if (lis[i][0] == "F"):
        t.forward(lis[i][1])
    if (lis[i][0] == "B"):
        t.backward(lis[i][1])
    if (lis[i][0] == "L"):
        t.left(lis[i][1])
    if (lis[i][0] == "R"):   
        t.right(lis[i][1])

turtle.done()