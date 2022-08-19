import turtle as t

def curvature():
	i=0
	for i in range(3):
			t.forward(150)
			t.right(90*i)		
		
t.bgcolor("white")
t.title("MyDesign")

colours=["blue","red","green","yellow","orange","black"]
t.pencolor("#285078")
t.pensize(5)
for j in range(6):
	t.left(0)
	t.left(60*j)
	t.fillcolor(colours[j])
	t.begin_fill()
	curvature()
	t.penup()
	t.home()
	t.pendown()
	t.end_fill()
t.done()