import turtle
color=["red","orange","yellow","green","blue","purple"]
sp=turtle.Pen()
turtle.bgcolor("black")

for i in range(360):
    sp.pencolor(color[i%6])
    sp.width(i/100 +1)
    sp.forward(i)
    sp.left(57)
