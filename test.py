import turtle

def drawSq(t, sz):
	for i in range(3):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
turtle_obj = turtle.Turtle()
turtle_obj.color('black')
turtle_obj.pensize(3)

drawSq(turtle_obj, 200)

wn.exitonclick()