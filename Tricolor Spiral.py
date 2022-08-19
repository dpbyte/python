import turtle as t
#t =turtle.Turtile()
s=t.Screen()
s.bgcolor("black")
t.width(4)
t.speed(50)

colors=["orange","white","green"]
for i in range(310):
	t.pencolor(colors[i%3])
	t.forward(i*4)
	t.right(121)
