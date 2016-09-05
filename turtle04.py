import turtle

def koch_fractal(t, side, order):
	if order == 0:
		t.forward(side)
	side  = side/3
	koch_fractal(t, side, order-1)
	t.left(60)
	koch_fractal(t, side, order-1)
	t.right(120)
	koch_fractal(t, side, order-1)
	t.left(60)
	koch_fractal(t, side, order-1)

def main():
	wn = turtle.Screen()
	wn.bgcolor('lightgreen')
	tess = turtle.Turtle()
	tess.color('black')
	tess.pensize(3)
	length = 300
	tess.penup()
	tess.backward(length/2.0)
	tess.pendown()
	koch_fractal(tess, length, 4)
	wn.exitonclick()

main()

