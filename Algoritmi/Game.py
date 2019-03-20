import turtle


a=turtle.Turtle()
a.speed(1)
a.up()
a.setx(-300)
a.sety(250)
a.down()
def myname():
	#bukva K
	a.up()
	#a.goto(-300,250)
	a.down()
	a.right(90)
	a.forward(33)
	a.left(135)
	a.forward(30)
	a.backward(30)
	a.right(90)
	a.forward(30)
	a.backward(30)
	a.right(45)
	a.forward(33)

	#bukva I
	a.up()
	#a.home()
	#a.goto(-300,250)
	a.forward(40)
	a.down()
	a.right(90)
	a.forward(66)
	a.left(160)
	a.forward(70)
	a.right(160)
	a.forward(66)

	#bukva R
	a.up()
	#a.home()
	#a.goto(-300,250)
	a.forward(80)
	a.down()
	a.right(90)
	a.forward(66)
	a.backward(66)
	a.left(90)
	a.forward(30)
	a.right(90)
	a.forward(30)
	a.right(90)
	a.forward(30)

	#bukva I
	a.up()
	#a.home()
	#a.goto(-300,250)
	a.forward(120)
	a.down()
	a.right(90)
	a.forward(66)
	a.left(160)
	a.forward(70)
	a.right(160)
	a.forward(66)

	#bukva L
	a.up()
	#a.home()
	#a.goto(-300,250)
	a.forward(175)
	a.down()
	a.right(110)
	a.forward(70)
	a.backward(70)
	a.left(35)
	a.forward(70)

	#bukva L
	a.up()
	#a.home()
	#a.goto(-300,250)
	a.forward(220)
	a.down()
	a.right(110)
	a.forward(70)
	a.backward(70)
	a.left(35)
	a.forward(70)
	
	a.up()
	a.left(80)
	a.right(180)
	a.forward(240)
	a.right(180)



for i in range(2):
	myname()

turtle.done()