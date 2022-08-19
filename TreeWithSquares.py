import turtle as t
def SubDesign():
	k=1
	for k in range(10):
		t.forward(50)
		t.left(45)
		t.backward(50)
def Design():
	i=1
	t.forward(150)
	for i in range(6):
				t.forward(150)
				SubDesign()	
t.bgcolor("white")
t.title("MyDesign")
colours=["blue","red","green","orange","yellow","black"]
t.speed(15)
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