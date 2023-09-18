# Yet another Robot in Python
# GPL v3 License
# Author: Armando Sousa, FEUP, asousa@fe.up.pt
# Date: 2023
# A simple robot in Python
#
# Useful links: 
# https://docs.python.org/3/library/turtle.html 
# https://pythonguides.com/python-turtle-mouse/
# https://docs.sympy.org/latest/index.html
#


import turtle
import random
import time
import math
import numpy
from sympy import Point2D, Line2D, Segment2D, intersection
# from typing import TypeVar

class my:
    """My algorithms for turtle graphics"""  

    global drawturtle 

    def __init__(self):
        vel, omega = 0, 0
        my.drawturtle = turtle.Turtle()
        my.drawturtle.hideturtle()
        my.drawturtle.color("red")
        my.drawturtle.speed(0)
        my.drawturtle.penup()
        

    def draw_seg(p1,p2, color="red"):
        my.drawturtle.penup()
        my.drawturtle.goto(p1[0],p1[1])
        my.drawturtle.pendown()
        my.drawturtle.color(color)
        my.drawturtle.goto(p2[0],p2[1])
        my.drawturtle.penup()

    def draw_point(p, color="red"):
        my.draw_seg([p[0][0]-10, p[0][1]-10], [p[0][0]+10, p[0][1]+10], color)
        my.draw_seg([p[0][0]-10, p[0][1]+10], [p[0][0]+10, p[0][1]-10], color)

    def perp( a ) :
        b = numpy.empty_like(a)
        b[0] = -a[1]
        b[1] = a[0]
        return b

    def line_intersect(p1,p2, p3,p4) :
        """ Return the intersection of two (infinit) lines p1-p2 and p3-p4
            Returns a false boolean if the lines don't intersect or the vector of the intersection point        
        """
        da = p2-p1
        db = p4-p3
        dp = p1-p3
        dap = my.perp(da)
        denom = numpy.dot( dap, db)
        num = numpy.dot( dap, dp )
        if (abs(denom) < 1e-5):
            return False # parallel lines

        return (num / denom.astype(float))*db + p3


    def seg_intersect(p1,p2, p3,p4) :
        """ Return the intersection of two line segments p1-p2 and p3-p4
            Returns a false boolean if the lines don't intersect or the vector of the intersection point        
        """
        ret = my.line_intersect(p1,p2, p3,p4)
        
        if ret is False: 
            return False
        
        min_x=min(p1[0],p2[0])
        max_x=max(p1[0],p2[0])
        min_y=min(p1[1],p2[1])
        max_y=max(p1[1],p2[1])
        if ( (ret[0]<min_x) or (ret[0]>max_x) or 
            (ret[1]<min_y) or (ret[1]>max_y) ):
            return False # out of segment 1

        min_x=min(p3[0],p4[0])
        max_x=max(p3[0],p4[0])
        min_y=min(p3[1],p4[1])
        max_y=max(p3[1],p4[1])
        if ( (ret[0]<min_x) or (ret[0]>max_x) or 
            (ret[1]<min_y) or (ret[1]>max_y) ):
            return False # out of segment 2
        
        return ret





#
# Yarp class
#
class Yarp(turtle.Turtle):
    """Yet Another Robot in Python (YARP)
    Drived from Turtle class
    Add Glow Unglow methods and Selected property"""

    vel=0
    omega=0

    def __init__(self):
        turtle.Turtle.__init__(self)
        self.Selected = False
        self.pensize(3)
        self.speed(0)
        self.shape("turtle")
        self.color("blue")
        self.fillcolor("")
        self.turtlesize(2,2,1)
        
    def move_fwd(self):
        self.forward(10)   

    def moved_rgt(self):
        self.right(10)

    def move_lft(self):
        self.left(10)

    def moves_bck(self):
        self.back(10)

    def byebye():
        #turtle.done()
        #turtle.bye()
        exit()
        

    def write_pos(self): 
        self.hideturtle()
        self.penup()
        prev_head=self.heading()
        self.setheading(90)
        self.forward(20)
        self.write(self.pos())
        self.back(20)    
        self.setheading(prev_head)
        self.pendown()
        self.showturtle()
        #turtle.write("Hello there!", align="center", font=("Arial Narrow", 10, "italic"))

    def put_at_mouse(x,y):
        rob1.write(f"({x},{y})")
        rob1.setpos(x,y)
        turtle.ondrag(rob1.put_at_mouse, 1)
        
    def clear2paths():
        rob1.clear()
        rob2.clear()
    
    def right_click(self, x, y):
        print(f" Rob1x: {self.xcor()} Rob1y: {self.ycor()} / Click_x: {x} Click_y: {y}")
        self.setheading(self.towards(x, y))
    
    def dragging(x, y): 
        print ("Dragging")
        rob1.ondrag(None)
        rob1.setheading(turtle.towards(x, y))
        turtle.goto(x, y)
        rob1.ondrag(rob1.dragging)

    def glow(self, x, y):
        print("Glow",self.__repr__(),f"x: {x} y: {y} ")
        self.fillcolor("red")
        
    def unglow(self, x, y):
        print("unglow",self.__repr__(),f"x: {x} y: {y} ")
        self.fillcolor("")

    def set_robot_pos(self, x : float, y : float , theta : float):
        self.setpos(x ,y)
        self.setheading(theta)

        
    def move_and_collide():
        # bail if the robot is out of the screen
        if rob1.xcor() > turtle.screensize()[0] or rob1.xcor() < -200 or rob1.ycor() > 200 or rob1.ycor() < -200:
            # Get turtle screen size
            print("Out of Bounds!")
            Yarp.byebye()
        # check if the robots collided           
        if math.dist(rob1.pos(),rob2.pos())<50:
            print("Robots collided!")
            Yarp.byebye()

        # Execute robot's movement
        rob1.left(rob1.omega/2)
        rob1.forward(rob1.vel/2)
        rob1.left(rob1.omega/2)
        rob1.forward(rob1.vel/2)

        rob2.left(rob2.vel/2)
        rob2.forward(rob2.vel/2)
        rob2.left(rob2.vel/2)
        rob2.forward(rob2.vel/2)

        rob1.vel+=1
        rob2.vel+=2
        rob1.omega+=random.randint(-10,10)
        rob2.omega+=random.randint(0,rob2.vel//10)

        turtle.ontimer(Yarp.move_and_collide, 500)
        
   

# Start of main code

rob1 = Yarp()
rob2 = Yarp()
rob2.shape("triangle")
rob2.color("green")
rob2.fillcolor("")
rob2.goto(100,100)


screen = turtle.Screen()
screen.title("YARP - Yet Another Robot in Python (python turtle)")
screen.bgcolor("lightgreen")

# Bind the arrow keys and other keys to the functions
turtle.listen()



nope=my()

#
# ~~~~~~ Start of Test line draw and intersection ~~~~~~
#

if False:            # Test line draw and intersection
    random.seed(10)

    for i in range(3):
        turtle.colormode(255)
        col = (random.randint(55,255), random.randint(0,155), random.randint(0,155))
    
        p1 = Point2D( random.randint(-200,200), random.randint(-200,200) )
        p2 = Point2D( random.randint(-200,200), random.randint(-200,200) )
        p3 = Point2D( random.randint(-200,200), random.randint(-200,200) )
        p4 = Point2D( random.randint(-200,200), random.randint(-200,200) )

        l1 = Line2D(p1,p2)
        l2 = Line2D(p3,p4)
        s1 = Segment2D(p1,p2)
        s2 = Segment2D(p3,p4)

        my.draw_seg(p1,p2, col)
        my.draw_seg(p3,p4, col)

        p_lin_cross = l1.intersection(l2)
        p_seg_cross = s1.intersection(s2)
        
        if len(p_seg_cross)>0:
            my.drawturtle.pensize(5)
            my.draw_point(p_seg_cross+[5,5], col)
            my.drawturtle.pensize(1)
            print("Segment Interception:", p_seg_cross[0].evalf())
        else:
            print("No Segment Interception")

        if len(p_lin_cross)>0:
            my.draw_point(p_lin_cross, col)
            print("Line Interception:", p_lin_cross[0].evalf())
            #print(f"Seg Dist: {s1.distance(p_lin_cross[0]):.2f}, {s2.distance(p_lin_cross[0])}")
            print("Seg1 Dist: {:.2f}".format(float(s1.distance(p_lin_cross[0]))))
            print("Seg2 Dist: {:.2f}".format(float(s2.distance(p_lin_cross[0]))))
        else:
            print("No Line Interception")

        time.sleep(1.0)
#
# ~~~~~~ End of Test line draw and intersection ~~~~~~
#

while True:
    print ("Starting loop")
    # Keyboard events Rob1
    turtle.onkeypress(rob1.move_fwd, 'Up')
    turtle.onkeypress(rob1.move_lft, 'Left')
    turtle.onkeypress(rob1.moved_rgt, 'Right')
    turtle.onkeypress(rob1.moves_bck, 'Down')
    turtle.onkeypress(rob1.write_pos, 'Return')
    # Keyboard events Rob2    
    turtle.onkeypress(rob2.move_fwd, 'w')
    turtle.onkeypress(rob2.move_lft, 'a')
    turtle.onkeypress(rob2.moved_rgt, 'd')
    turtle.onkeypress(rob2.moves_bck, 's')
    turtle.onkeypress(rob2.write_pos, ' ')
    # Keyboard events common
    turtle.onkeypress(Yarp.byebye  , 'Escape')
    turtle.onkeypress(Yarp.clear2paths, 'c')
    turtle.ontimer(Yarp.move_and_collide, 500)

    # Mouse events
    rob1.onclick(rob1.glow, 1)
    rob1.onrelease(rob1.unglow, 1, True)
    rob2.onclick(rob2.glow, 1)
    rob2.onrelease(rob2.unglow, 1, True)
    #turtle.ondrag(turtle.goto,1, True)
    turtle.onscreenclick(rob1.right_click, 3, True)
    turtle.onscreenclick(rob2.right_click, 2, True)

    time.sleep(1)

    # Keep window open
    screen.mainloop()
    
        
   
  
# Fim Código principal



