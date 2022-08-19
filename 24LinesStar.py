
import turtle as t
import time
#t =turtle.Turtile()
s=t.Screen()
s.bgcolor("black")
t.width(4)
t.speed(5)
colors=["green","white","orange"]
t. pencolor ("red")

for i in range(24):
	t. backward (100)
	t. right (15)
	t.forward(100)

xlg=t.xcor()
ylg=t.ycor()
m=t.position ()
for i in range(1,4):
	xlg=m[0]
	for j in range (0,3):
		t.penup()
		t.goto(xlg+(100),ylg+50)
		xlg=t.xcor()
		ylg=t.ycor()
		t.pendown()
		t.color(colors[j])
		t.circle(-30,90)
		t.circle (30,-90)
		t.right (180)
	"""
	for i in range(24):
		t.backward(10)
		t.right(15)
		t.forward(10)
	"""	