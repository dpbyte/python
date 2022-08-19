import turtle as t
def SubDesign():
	k=1
	for k in range(10):
		t.forward(10)
		t.left(10)
		t.backward(10)
def Design():
	i=1
	t.forward(150)
	for i in range(20):
				t.forward(100)
				SubDesign()	
t.bgcolor("white")
t.title("MyDesign")
colours=["blue","red","green","orange","yellow","black"]
#t.pencolor("#285078")
t.pensize(5)
t.left(270)
t.forward(500)
t.home()
t.left(0)
for j in range(6):
	t.pencolor(colours[j])
	t.left(0)
	t.left(60*j)
	t.forward(50)
	#t.fillcolor(colours[j])
	#t.begin_fill()
	Design()
	t.left(90)
	#t.end_fill()
	t.penup()
	t.home()
	t.pendown()
t.done()