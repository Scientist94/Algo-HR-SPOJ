import turtle 

def drawSpiral(t, angle):
	len = 1
	for i in range(100):
		t.forward(len)
		t.right(angle)
		len += 2

wn = turtle.Screen()
wn.bgcolor("lightgreen")

alex = turtle.Turtle()
alex.color("black")
alex.pensize(2)
alex.speed(3)

alex.pendown()
drawSpiral(alex, 89)

wn.exitonclick()