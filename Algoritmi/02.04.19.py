import turtle


a=turtle.Turtle()
a.speed(100)
a.pensize(2)
def myname():
	a.up()
	a.setpos(-100,200)
	print (a.xcor())
	print (a.ycor())
	a.down()
	for i in range(5):
		# a.right(16.37)
		# a.forward(10)
		if i%2==0:
			for i in range(10):
				a.right(16.37)
				a.forward(10)
			a.setheading(180)
		else :
			for i in range(10):
				a.left(16.37)
				a.forward(10)
			a.setheading(0)
	for i in range(10):
			a.right(16.35)
			a.forward(50)

	# for i in range(10):
	# 	a.left(13.37)
	# 	a.forward(10)
	# a.setheading(0)
	# for i in range(10):
	# 	a.right(16.37)
	# 	a.forward(10)
	# for i in range(10):
	# 	a.left(13.37)
	# 	a.forward(10)
	# for i in range(10):
	# 	a.right(16.37)
	# 	a.forward(10)
		
			


for i in range(20):
	myname()
	a.setheading(0)
print (a.xcor())
print (a.ycor())
turtle.done()