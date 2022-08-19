import turtle as t

def curvature():
	i=1
	for i in range(3):
			t.forward(150)
			t.right(90)		
		
t.bgcolor("white")
t.title("MyDesign")

colours=["blue","red","green","orange","yellow","black"]
#t.pencolor("#285078")
t.pensize(5)
for j in range(4):
	t.pencolor(colours[j])
	t.left(0)
	t.left(90*j)
	t.forward(100)
	t.fillcolor(colours[j])
	t.begin_fill()
	curvature()
	t.left(90)
	t.end_fill()
	t.penup()
	t.home()
	t.pendown()

t.done()