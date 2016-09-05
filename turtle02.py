import turtle

def drawSq(t, sz):
	for i in range(4):
		t.forward(sz)
		t.left(90)
	# t.right(90)
	# t.forward(10)
	# t.left(90)
	# t.forward(10)


wn = turtle.Screen()
wn.bgcolor('lightgreen')
t_obj = turtle.Turtle()
t_obj.color('black')
t_obj.pensize(3)

size = 20

for i in range(5):
	drawSq(t_obj, size)
	t_obj.penup()
	t_obj.right(90)
	t_obj.forward(10)
	t_obj.right(90)
	t_obj.forward(10)
	t_obj.right(180)
	t_obj.pendown()
	size += 20

wn.exitonclick()