import turtle

def drawSq(t, sz, n):
	for i in range(n):
		t.right(90 + 18*i)
		for j in range(4):
			t.forward(sz)
			t.right(90)
		t.setheading(0)


wn = turtle.Screen()
alex = turtle.Turtle()
alex.color("black")
wn.bgcolor("lightgreen")
alex.pensize(3)

drawSq(alex, 200, 20)
wn.exitonclick()