import turtle as t

def curvature():
	i=0
	for i in range(50,60):
			t.forward(i*5)
			t.left(10)
			t.backward(i*5)		
		
t.bgcolor("white")
t.title("MyDesign")

colours=["blue","red","green","yellow"]
for j in range(4):
	t.left(0)
	t.left(90*j)
	t.fillcolor(colours[j])
	t.begin_fill()
	curvature()
	t.penup()
	t.home()
	t.pendown()
	t.end_fill()
t.done()