import turtle

mysp=turtle.Screen().bgcolor("pink")
spiral=turtle.Turtle()
size=0

while True:
    for i in range(4):
        spiral.fd(size+1)
        spiral.left(90)
        size-=5
    size+=1