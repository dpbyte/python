import turtle as t
def SubDesign():
	k=1
	for k in range(10):
		t.forward(50)
		t.left(5*k)

def Design():
	i=1
	for i in range(2):
			t.forward(50)
			SubDesign()	
		
t.bgcolor("white")
t.title("MyDesign")
colours=["blue","red","green","orange","yellow","black"]
#t.pencolor("#285078")
t.pensize(5)
for j in range(4):
	t.pencolor(colours[j])
	t.left(0)
	t.left(90*j)
	t.forward(50)
	t.fillcolor(colours[j])
	t.begin_fill()
	Design()
	t.left(90)
	t.end_fill()
	t.penup()
	t.home()
	t.pendown()
t.done()