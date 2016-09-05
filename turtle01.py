import turtle

def drawSq(t, sz):
	for i in range(4):
		t.forward(sz)
		t.left(90)

wn = turtle.Screen()
wn.bgcolor('lightgreen')
turtle_obj = turtle.Turtle()
turtle_obj.color('black')
turtle_obj.pensize(3)

for i in range(5):
	drawSq(turtle_obj, 20)
	turtle_obj.penup()
	turtle_obj.forward(40)
	turtle_obj.pendown()

wn.exitonclick()