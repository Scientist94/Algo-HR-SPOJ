import turtle 

def StarPattern(t, sz):
	for i in range(5):
		t.forward(sz)
		t.left(216)

def multipleStars(t, len):
	for i in range(5):		
		t.penup()		
		t.forward(350)
		t.right(144)
		t.pendown()
		StarPattern(t, len)


wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("black")
tess.pensize(3)
multipleStars(tess, 350)
wn.exitonclick()