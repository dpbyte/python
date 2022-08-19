import turtle as t
import time

s=t.Screen()
s.bgcolor("gray")
t.width(4)
t.speed(10)
t.turtlesize(5)

def person(selute,cp):
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
		
		t.turtlesize(3)
		#hand motion
		t.right(70)
		t.forward(70)
		time.sleep(1)
		t.color("gray")
		t.backward(70)
		t.left(70)
		t.color("black")
		#hand motion
		t.right(90)
		t.forward(80)
		time.sleep(1)
		t.color("gray")
		t.backward(80)
		t.left(90)
		t.color("black")
		#hand motion
		t.right(115)
		t.forward(90)
		time.sleep(1)
		t.color("gray")
		t.backward(90)
		t.left(115)
		t.color("black")
		#Selute Posision
		t.right(135)
		t.forward(100)
		t.turtlesize(3)
		t.stamp()
		time.sleep(2)
	else:
		#Normal Left hand
		t.right(45)
		t.forward(100)
		t.goto(cp)
		time.sleep(2)

colors=["green","white","orange"]

#Green
t.pen(fillcolor=colors[0],pencolor=colors[0])
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

#White
t.pendown()
t. pencolor (colors[1])
t.color(colors[1])
t.begin_fill()
t.forward (300)
t.right(90)
t.forward (100)
t.right(90)
t.setx(0)
t.sety(200)
t.end_fill()

#Orange
t. pencolor (colors[2])
t.color(colors[2])
t.begin_fill()
t.right(180)
t.forward (300)
t.right(90)
t.forward (100)
t.right(90)
t.forward (300)
t.end_fill()
t.penup()


#Ashoka Chakra
t.backward (150)
t. pencolor ("black")
t.left(90)
t.forward (1)
t.pendown()
t.right(90)
t.circle (50)

#CenterPoint of Ashoka Chakra 
t.penup()
t.left(90)
t.forward(60)
t.left(90)
t.pendown()
t.circle(10)
t.penup()
t.pendown()
t.right(270)
t.forward(60)

for i in range(24):
	t.backward(50)
	t.right(15)
	t.forward(50)
	t.left(90)
	t.circle (3)
	t.right(90)
t.penup()

#Pole Design
t.setx(0)
t.sety(100)

t.pendown()
t. pencolor (colors[2])
t.forward (100)
t.right(45)
t.circle(10)
t.left(90)
t. forward (10)

t.right (225)

t.width(10)
t.forward(315)
t.left(135)
t.width(4)
t.forward(10)
t.backward(10)
t.right(135)
t.width(10)
t. pencolor (colors[1])
t. forward (300)
t. pencolor (colors[0])
t. forward (300)

#Flag Stage Design
t.width(4)
t.left(90)
t.pencolor(colors[2])
t. color(colors[2])
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

t. pencolor (colors[1])
t.color(colors[1])

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
t.color(colors[0])
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

#Flying Flowers 
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

t.color("black")
t.penup()
t.right(180)
t.forward(100)
t.right(90)
t .forward(50)
t.pendown()
t.right(90)

#Person Function call for National Flag Selute
person(1,t.position())

time.sleep(20)
