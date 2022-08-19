import turtle as t
import time as time

def circleincircle():
	t.circle(200)
	t.begin_fill()
	t.circle(160)
	t.end_fill()

t.title("My Turtile Program")
Colours=["black","red","green","blue"]
for i in range(4):
	t.pen(fillcolor=Colours[i])
	circleincircle()
	t.right(90)
	
time.sleep(5)
t.done()