import turtle

turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(300,300)

poly=turtle.Turtle()

sides=int(input("Enter the number of sides: "))
len=int(input("Enter the length of sides: "))
angle=360/sides

for i in range(sides):
    poly.forward(len)
    poly.right(angle)
    
turtle.done()
