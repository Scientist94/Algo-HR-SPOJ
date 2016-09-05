import turtle

def star(t, n, d):
	if n%2 != 0:
		for i in range(n):
			angle = 180.0 - 180.0 / n
			t.forward(d)
			t.right(angle)
			t.forward(d)
	else:
		pass

wn = turtle.Screen()
wn.bgcolor("lightgreen")
t_obj = turtle.Turtle()
t_obj.color("black")
t_obj.pensize(2)
t_obj.speed(2)
star(t_obj, 39, 250)
wn.exitonclick()