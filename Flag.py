import turtle as t
import time
#t =turtle.Turtile()
s=t.Screen()
s.bgcolor("gray")
t.width(4)
t.speed(50)
t.turtlesize(5)


def person(selute,cp):
	
	#cp=t.position ()
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
	
	
	#right hand 
	t.left(45)
	t.forward (100)
	t.goto(cp)
	t.right(90)
	
	#head
	t.left(135)
	t.circle (40)
	t.right(90)
	
	if selute==1:
		#leftselute
		m=t. position ()
		t.right(90)
		t.forward(100)
		
		t.right(70)
		t.forward(70)
		t.color("gray")
		t.backward(70)
		t.left(70)
		t.color("black")
		
		t.right(90)
		t.forward(80)
		t.color("gray")
		t.backward(80)
		t.left(90)
		t.color("black")
		
		t.right(115)
		t.forward(90)
		t.color("gray")
		t.backward(90)
		t.left(115)
		t.color("black")
		
		t.right(135)
		t.forward(100)
		t.turtlesize(3)
		t.stamp()
		t.penup()
#		t.goto(m)
#		t.right(180)
		t.pendown()
		#"""
	else:
		#"""
		#left hand
		t.right(45)
		t.forward(100)
		t.goto(cp)
		#"""
	"""	
	#right hand 
	t.left(90)
	t.forward (100)
	t.goto(cp)
	
	#head
	t.left(45)
	t.circle (40)
	"""

colors=["green","white","orange"]
#border=["red"]
"""
for i in range(310):
	t.pencolor(colors[i%3])
	t.forward(i*4)
	t.right(121)
"""
"""
for i in range(4):
	for j in range(1,5):
		t. pencolor (border[0])
		t.forward (i*100)
		t.right(90)
"""
#t. pencolor (colors[0])
t.pen(fillcolor="green",pencolor=colors[0])
t.begin_fill()
t.forward (300)
t.right(90)
t.forward (100)
t.right(90)
t.forward (300)
t.right(90)
t.forward (100)
t.right(90)
t.end_fill()
t.penup()
t.setx(0)
t.sety(100)

t.pendown()
t. pencolor (colors[1])
t.color("white")
t.begin_fill()
t.forward (300)
t.right(90)
t.forward (100)
t.right(90)
t.setx(0)
t.sety(200)
t.end_fill()

t. pencolor (colors[2])
t.color("orange")
t.begin_fill()
t.right(180)
t.forward (300)
t.right(90)
t.forward (100)
t.right(90)
t.forward (300)
t.end_fill()
t.penup()


t.backward (150)

t. pencolor ("black")

t.left(90)
t.forward (1)
t.pendown()
t.right(90)
t.circle (50)
t.right(90)
#t. backward (45)
#t.right(43)
t.penup()
#t.backward(5)
t.pendown()
#t.left(43)

for i in range(24):
	t.backward(50)
	t.right(15)
	t.forward(50)
	t.left(90)
	t.circle (3)
#	t.circle(10,-90)
#	t.circle (-10,90)
	t.right(90)
t.penup()
	
t.setx(0)
t.sety(100)

t.pendown()
t. pencolor ("orange")
t.forward (100)
t.right(45)
t.circle(10)
t.left(90)
t. forward (10)

t.right (225)
#t. forward (15)
t.width(10)
t.forward(315)
t.left(135)
t.width(4)
t.forward(10)
t.backward(10)
t.right(135)
t.width(10)
t. pencolor ("white")
t. forward (300)
t. pencolor ("green")
t. forward (300)
t.width(4)
t.left(90)
t.pencolor("orange")
t. color("orange")
t.begin_fill()
t.forward(100)
t.right(90)
t.forward(50)
t.right(90)
t.forward(200)
t.right(90)
m=t.position ()
t. forward (50)
t.right(90)
t.forward(100)
t.end_fill()
t.goto(m)

t. pencolor (colors[2])
t.color("white")

t.begin_fill()
t.right(180)
t.forward (100)
t.left(90)
t.forward (50)
t.left(90)
t.forward (400)
m=t.position()
t.left(90)
t. forward (50)
t.left(90)
t.forward(300)
t.end_fill()

t.goto(m)
t.color("green")
t.begin_fill()
t.backward(100)
t.left(90)
t.forward(50)
t.right(90)
lg=t. position ()
t. forward (600)
rg=t.position ()
t.right(90)
t. forward (50)
t.right(90)
t.forward(200)
t.end_fill()
t.penup()
t.goto(lg)
t.forward(150)
lg=t.position()
xlgf=t.xcor()
ylgf=t.ycor()

t.pendown()
xlgf=t.xcor()-400
ylg=t.ycor()+800
m=t.position ()
for i in [4,3,2,1,0]:
	xlg=xlgf
	for j in [2,1,0]:
		t.penup()
		t.goto(xlg+(100),ylg-(50))
		xlg=t.xcor()
		ylg=t.ycor()
		t.pendown()
		t.color(colors[j])
		t.circle(-30,90)
		t.circle (30,-90)
		t.right (180)
t.penup()
t.goto(rg)
t.pendown()
"""
xlg=rg[0]
ylg=rg[1]
m=t.position ()
for i in range(1,5):
	xlg=m[0]
	for j in range (0,3):
		t.penup()
		t.goto(xlg-(100),ylg+50)
		xlg=t.xcor()
		ylg=t.ycor()
		t.pendown()
		t.color(colors[j])
		t.circle(-30,90)
		t.circle (30,-90)
		t.right (180)
"""
t.color("black")
t.penup()
t.right(180)
t.forward(100)
t.right(90)
t .forward(50)
t.pendown()
t.right(90)
person(1,t.position())
time.sleep(20)
