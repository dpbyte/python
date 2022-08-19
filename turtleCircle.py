import turtle as t
import random as r
t.bgcolor("black")
t.speed (0)
colours=["white","blue","green","yellow","red"]
for i in range(200):
	t.circle(i+20)
	#t.forward(i)
	t.left(20)
	#t.pencolor(colours[r.randint(0,4)])
	#t.pencolor(colours[3])
	t.pencolor(colours[4])
	
t.done()
r.done()
