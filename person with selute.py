import turtle as t
import time
#t =turtle.Turtile()
s=t.Screen()
s.bgcolor("grey")
t.width(4)
t.speed(5)


colors=["green","white","orange"]

selute=1
cp=t.position ()
#right leg
t.right(45)
t.forward(100)
t.right(135)
t.forward(50)
t.goto(cp)

#left leg
t.left(45)
t.forward (100)
t.left(135)
t.forward(50)
t.goto(cp)

#shoulder
t.right(90)
t.backward(200)
cp=t.position ()

if selute==1:
	#leftselute
	m=t. position ()
	t.right(90)
	t.forward(100)
	t.right(135)
	t.forward(100)
	t.penup()
	t.goto(m)
	t.right(180)
	t.pendown()
	#"""
else:
	#"""
	#left hand
	t.right(45)
	t.forward(100)
	t.goto(cp)
	#"""
	
#right hand 
t.left(90)
t.forward (100)
t.goto(cp)

#head
t.left(45)
t. circle (40)

time.sleep(20)