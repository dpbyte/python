import turtle as t

def curvature():
	i=0
	for i in range(60):
			t.forward(i)
			t.left(10)
			t.backward(i+20)			
		
t.bgcolor("white")
t.title("MyDesign")
t.fillcolor("blue")
t.begin_fill()
curvature()
t.penup()
t.home()
t.pendown()
t.end_fill()

t.left(0)
t.left(90)
t.begin_fill()
t.fillcolor("red")
curvature()
t.penup()
t.home()
t.pendown()
t.end_fill()

t.left(0)
t.left(180)
t.begin_fill()
t.fillcolor("green")
curvature()
t.penup()
t.home()
t.pendown()
t.end_fill()

t.left(0)
t.left(270)
t.begin_fill()
t.fillcolor("yellow")
curvature()
t.penup()
t.home()
t.pendown()
t.end_fill()

t.left(0)
t.fillcolor("blue")
t.begin_fill()
curvature()
t.penup()
t.home()
t.pendown()
t.end_fill()

t.done()