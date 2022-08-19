import turtle as t

def curvature():
	i=0
	for i in range(6):
			t.forward(100)
			t.right(90*i)		
		
t.bgcolor("white")
t.title("MyDesign")

colours=["blue","red","green","yellow"]
t.pencolor("red")
t.pensize(20)
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