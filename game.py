#############################################################################################################################################
#########        ######   #####  ######  ####  ####  ############  #######  #########     ###########       #################################
############  ######## ##  ####  #  ###  ####  ### ##############  #######  ########  ###  ##########   #    ################################
############  #######       ###  ##  ##  ####  #  ###############  ##   ##  #######         #########     ###################################
############  ######  #####  ##  ####    ####  ####  #############    ##   #######  #######  ########  ##   ################################# 
############  #####  #######  #  #####   ####  #####  #############  ####  ######  #########  #######  ####   ###############################
#############################################################################################################################################

############################################################# TANK WAR V 1.0 ################################################################
from turtle import bgpic
from turtle import title
from turtle import screensize 
from turtle import bgcolor
import turtle as t
from math import*
from random import*

#######################         registers shapes for turtle      ############################################################################
t.speed('fastest')
title('Tank-War v 1.0 ')
screensize(1024,700)
bgpic('bg.gif')
bgcolor('black')
t.ht()
t.register_shape('30016.gif')
t.register_shape('tankr.gif')
t.register_shape('target1.gif')
##################################### Title and Screen #######################################################################################
splash=t.Turtle()
splash.shape('30016.gif')
ww=t.Turtle()
ww.color('yellow')
ww.ht()
ww.up()
ww.goto(-150,0)
ww.down()
ww.write('TANK WAR v 1.0 ',font=('Arial',36,'bold'))
for i in range(10):
	splash.rt(90)
box1=t.Turtle()
box1.ht()
box1.up()
box1.goto(0,-300)
box1.fillcolor('black')
box1.shape('square')
box1.shapesize(15,200,1)
box1.st()
########################   'Best viewed in full screen '   ####################################################################################
w=t.Turtle()
w.color('white')
w.ht()
w.up()
w.goto(-200,0)
w.down()
splash.ht()
ww.undo()
w.write('Best viewed in full screen ',font=('Arial',25,'normal'))
###########################    Tank nozzle           ###########################################################################################
n1=t.Turtle()
n1.ht()
n1.fillcolor(0,0,0)
n1.shape('square')
n1.shapesize(0.3,2.5,1)
n1.up()
n1.lt(45)
n1.goto(-562.0,-65.0)
n1.st()

####################### Target #################################################################################################################
tar=t.Turtle()
tar.ht()
tar.shape('target1.gif')
tankl=t.Turtle()
tankl.ht()
tankl.shape('tankr.gif')
tankl.up()
tar.up()
tar.goto(530,-140)
tankl.goto(-679,-44)
tankl.st()
tar.st()

############## This part was used to find the coordinates of diff. turtles #####################################################################
def cor(x,y):
	t.up()
	t.goto(x,y)
	t.down()
	t.color('white')
	t.write(str(x)+' , '+str(y))
#t.onscreenclick(cor)

################### Texts appearing on the screen ##############################################################################################
wrt=t.Turtle()
wrt.color('white')
wrt.ht()
wrt.up()
wrt.goto(-618.0,-212.0)
wrt.down()
wrt.write('YOU',font=('Arial',14,'bold'))
#---------------------------------------------------------#
wrt.color('white')
wrt.ht()
wrt.up()
wrt.goto(508.0,-212.0)
wrt.down()
wrt.write('COMPUTER',font=('Arial',14,'bold'))
#---------------------------------------------------------#
wrt.color('red')
wrt.ht()
wrt.up()
wrt.goto(-618.0,-350)
wrt.down()
wrt.write('FIRE',font=('Arial',16,'bold'))
#---------------------------------------------------------#
wrt.color('yellow')
wrt.ht()
wrt.up()
wrt.goto(-20,-350.0)
wrt.down()
wrt.write('POWER',font=('Arial',12,'normal'))
#---------------------------------------------------------#
wrt.color('white')
wrt.ht()
wrt.up()
wrt.goto(-206.0,-350.0)
wrt.down()
wrt.write('0',font=('Arial',8,'normal'))
#---------------------------------------------------------#
wrt.color('white')
wrt.ht()
wrt.up()
wrt.goto(194.0,-350.0)
wrt.down()
wrt.write('100',font=('Arial',8,'normal'))
#---------------------------------------------------------#
wrt.color('white')
wrt.ht()
wrt.up()
wrt.goto(-410,-350.0)
wrt.down()
wrt.write('ANGLE',font=('Arial',12,'normal'))
#---------------------------------------------------------#
wrt.color('white')
wrt.ht()
wrt.up()
wrt.goto(-520,-350.0)
wrt.down()
wrt.write('MOVE',font=('Arial',12,'normal'))
###################### controls ######################################################################################################

def theta1(x,y):
	if n1.heading()<90. and n1.heading()>0.:
		n1.lt(1.)
	if n1.heading() >=90. :
		n1.rt(2.)
	
c1=t.Turtle()
c1.ht()
c1.lt(90)
c1.fillcolor('green')
c1.shapesize(3,3,1)	
tankl.rt(1)
c1.up()
c1.goto(-380.0,-241.0)
c1.down()
c1.st()
c1.onclick(theta1)
#---------------------------------------------------------------------------------------------------------------------------#
def theta2(x,y):
	if n1.heading()<90. and n1.heading()>0.:
		n1.rt(1.)
	elif n1.heading()<=0.:
		n1.lt(2.)
	ang.append(n1.heading())
c2=t.Turtle()
c2.ht()
c2.rt(90)
c2.fillcolor('yellow')
c2.shapesize(3,3,1)	
c2.up()
c2.goto(-380.0,-300.0)
c2.down()
c2.st()
c2.onclick(theta2)
#########################    control for movements    ############################################################################

def moveforward(x,y):
	if tankl.xcor()<=-579. and tankl.xcor()>=-680.: 
		n1.goto(n1.xcor()+5,n1.ycor())
		tankl.goto(tankl.xcor()+5,tankl.ycor())
	elif tankl.xcor()>-579. :
		n1.goto(n1.xcor()-7,n1.ycor())
		tankl.goto(tankl.xcor()-7,tankl.ycor())
	
mf=t.Turtle()
mf.ht()
mf.fillcolor('blue')
mf.shapesize(3,4,1)	
mf.up()
mf.goto(-450.0,-270.0)
mf.down()
mf.st()
mf.onclick(moveforward)
#-------------------------------------------------------------------------------------------------------------------------------#
def movebackward(x,y):
	if tankl.xcor()<=-579. and tankl.xcor()>=-680.:
		n1.goto(n1.xcor()-5,n1.ycor())
		tankl.goto(tankl.xcor()-5,tankl.ycor())
	elif tankl.xcor()<-680. :
		n1.goto(n1.xcor()+7,n1.ycor())
		tankl.goto(tankl.xcor()+7,tankl.ycor())
	coor.append(tankl.xcor())
mb=t.Turtle()
mb.ht()
mb.rt(180)
mb.fillcolor('blue')
mb.shapesize(3,4,1)	
mb.up()
mb.goto(-550.0,-270.0)
mb.down()
mb.st()
mb.onclick(movebackward)


#------------------------power buttons--------------------------------------------------------------------------------------------#
box2=t.Turtle()
box2.ht()
box2.up()
box2.goto(0,-300)
box2.fillcolor('blue')
box2.shape('square')
box2.shapesize(2,20,1)
box2.st()
#---------------------------------------------------------------------------------------------------------------------------------#
box3=t.Turtle()
box3.ht()
box3.up()
box3.goto(0,-300)
box3.fillcolor('red')
box3.shape('square')
box3.shapesize(2,1,1)

box3.st()
pos=[]
def power(x,y):
	
	if x<194 and x>-206 :  
		box3.goto(x,-300)
	elif x>=194:
		box3.goto(194,-300)
	elif x<=-206:
		box3.goto(-206,-300)
pos.append((box3.xcor()+206)/4.0)
box3.ondrag(power)
w.undo()

#################################### game dynamics ###################################################################################
g=9.8
k=0.00000
m=1.

y=-65.0
r=1000.0
vxc=(r*g/2**0.5)**1/2.
vyc=60.
dt=0.04
xc=-562.0
yc=-65.0
c = t.Turtle()
c.shapesize(0.5,0.5,1)
p=t.Turtle()	
p.ht()
p.up()
p.shape('square')
p.goto(617,-161.0)
p.pensize(10)
p.down()
p.color('blue')
p.fd(-606)
p.color('red')
p.fd(-606)
p.fd(606)
p.st()
p.fillcolor('black')
www=t.Turtle()
def fr(x,y):
	c.shape('circle')
	c.fillcolor('red')
	vx=abs((box3.xcor()+206)*cos((pi/180)*n1.heading()))
	vy=abs((box3.xcor()+206)*sin((pi/180)*n1.heading()))
	
	#__________________________________________________ kinematics_________________________________________________________________________________________#
	k=0.001 # changes the viscosity in air #
	m=1.  # mass of cannon ball
	tf=100
	dt=0.05
	t=0
	g=9.8 # acceleration due to gravity

	x=n1.xcor()
	y=n1.ycor()
	c.up()
	c.ht()

	v=(vx**2.+vy**2.)**0.5	
	ax=-(k/m)*v*vx
	ay=-g-(k/m)*v*vy
	vx+=ax*dt
	vy+=ay*dt
	x+=vx*dt+0.5*ax*dt*dt
	y+=vy*dt+0.5*ay*dt*dt
	c.goto(x,y)
	c.st()
	while y>-95:
		c.goto(x,y)
		v=(vx**2.+vy**2.)**0.5	
		ax=-(k/m)*v*vx
		ay=-g-(k/m)*v*vy
		vx+=ax*dt
		vy+=ay*dt
		x+=vx*dt+0.5*ax*dt*dt
		y+=vy*dt+0.5*ay*dt*dt
		t+=dt
	for j in range(10):
			r=random()
			c.shape('circle')
			c.shapesize(10*r,10*r,1)
			c.fillcolor('red')
			c.fd(1)
			c.bk(1)
			c.fillcolor('yellow')
	c.ht()
	c.shapesize(0.5,0.5,1)
	yy=tar.ycor()
	xx1=tankl.xcor()
	xx2=tar.xcor()
	
	print tar.xcor()
	print c.xcor()
	if c.xcor()<=(tar.xcor()+76) and c.xcor()>=(tar.xcor()-80):
		p.color('red')
		p.fd(100)
		
	else:
		p.color('blue')
		p.fd(-100)
	tar.ht()
	tar.goto(randint(-200,580),yy)
	tar.st()
		
	if p.xcor()>= 580.0:
		
		www.color('yellow')
		www.ht()
		www.up()
		www.goto(-200,0)
		www.down()
		www.write('!!! YOU WIN  !!! ',font=('Arial',36,'bold'))
		fire.onclick(None)
		for i in range(50):
			wrt.undo()
		fire.ht()
		mf.ht()
		mb.ht()
		c1.ht()
		c2.ht()
		box2.ht()
		box3.ht()
		quit()
	elif p.xcor()<=-536:
		
		www.color('yellow')
		www.ht()
		www.up()
		www.goto(-200,0)
		www.down()
		www.write('!!! YOU LOSE !!! ',font=('Arial',36,'bold'))
		fire.onclick(None)
		for i in range(50):
			wrt.undo()
		fire.ht()
		mf.ht()
		mb.ht()
		c1.ht()
		c2.ht()
		box2.ht()
		box3.ht()
		quit()	 
	
################################################################    fire    ##################################################################			
fire=t.Turtle()
fire.ht()			
fire.shape('circle')			
fire.fillcolor('red')		
fire.shapesize(3,3,1)
fire.up()				
fire.goto(-600.0,-280.0)
fire.down()		
fire.st()		
fire.onclick(fr)
			
################################################################################################################################################
###############################################################    Thank you     ###############################################################
################################################################################################################################################

raw_input()

