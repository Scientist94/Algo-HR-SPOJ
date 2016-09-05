import turtle

def drawPoly(someturtle, somesides, somesize):
	for i in range(somesides):
		someturtle.forward(somesize)
		someturtle.left(360/somesides)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
tess = turtle.Turtle()
tess.color('black')
tess.pensize(3)

sides = 12   ##generalise to ask for input
size = 50  ##generalise to ask for input

tess.pendown()
drawPoly(tess, sides, size)

wn.exitonclick()

