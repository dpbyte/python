import turtle as t
import random as r
t.bgcolor("black")
t.speed (0)
colours=["white","blue","green","yellow","red"]
t.begin_fill()
for i in range(180):
	#t.circle(i+20)
	#t.forward(i)
	t.forward(i+200)
	t.left(20)
	t.backward(200)
	t.backward(200)
	t.left(20)
	t.forward(i+200)
	#t.pencolor(colours[r.randint(0,4)])
	#t.pencolor(colours[3])
	t.pencolor(colours[4])
	
t.end_fill()
t.done()
r.done()
