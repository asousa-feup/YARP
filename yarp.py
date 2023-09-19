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
# Python types: https://peps.python.org/pep-0484/  and https://docs.python.org/3/library/typing.html and https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html


import turtle
import random
import time
import math
import numpy
from sympy import Point2D, Line2D, Segment2D, intersection
# from varname import nameof # https://pypi.org/project/varname/ # https://stackoverflow.com/questions/18425225/getting-the-name-of-a-variable-as-a-string

# Initializations (global stuff) for MyDraw class
hidden_turtle = turtle.Turtle()
hidden_turtle.hideturtle()
hidden_turtle.color("orange")
hidden_turtle.speed(0)
hidden_turtle.penup()



#
# ~~~~~~ Start of MyDraw class ~~~~~~
#
class MyDraw:
    """Algorithms for (robotics related) drawings (by using a hidden) turtle graphics """  

    def __init__(self):
        hidden_turtle.hideturtle()
        hidden_turtle.color("orange")
        hidden_turtle.speed(0)
        hidden_turtle.penup()
        

    def draw_seg(p1,p2, color="orange", pensize : int=1):
        prev_pensize = hidden_turtle.pensize()
        prev_color = hidden_turtle.color()
        hidden_turtle.pensize(pensize)
        hidden_turtle.penup()
        hidden_turtle.goto(p1[0],p1[1])
        hidden_turtle.pendown()
        hidden_turtle.color(color)
        hidden_turtle.goto(p2[0],p2[1])
        hidden_turtle.penup()
        hidden_turtle.pensize(prev_pensize)
        hidden_turtle.color(prev_color[0], prev_color[1])
        

    def draw_point(p, color : str ="orange", pensize : int=1):
        MyDraw.draw_seg([p[0][0]-10, p[0][1]-10], [p[0][0]+10, p[0][1]+10], color, pensize)
        MyDraw.draw_seg([p[0][0]-10, p[0][1]+10], [p[0][0]+10, p[0][1]-10], color, pensize)


    def draw_quad(p1,p2,p3,p4, color="red"):
        MyDraw.draw_seg(p1,p2, color)
        MyDraw.draw_seg(p2,p3, color)
        MyDraw.draw_seg(p3,p4, color)
        MyDraw.draw_seg(p4,p1, color)

#
# ~~~~~~~~ Yarp class ~~~~~~~~
#
class Yarp(turtle.Turtle):
    """Yet Another Robot in Python (YARP) -- Drived from Turtle class
    Add Glow Unglow methods and Selected property"""

    vel :   float = 0.0
    omega : float = 0.0
    yarp_time :  float = 0.0


    def __init__(self):
        turtle.Turtle.__init__(self)
        vel=0.0
        omega=0.0
        yarp_time = 0.0
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
        exit() #TODO: Fix this... this is violent... is there a better way?
        

    def write_pos(self): 
        self.hideturtle()
        self.write(f"({self.pos()[0]:.2f} , {self.pos()[1]:.2f})".format(self.pos()[0],self.pos()[1]), align="center", font=("Arial Narrow", 10, "italic"))
        self.showturtle()

    def place_robot_at(self, x,y):
        print(f"(Will place robot at mouse coords {x},{y})")
        self.setpos(x,y)
        
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
        #print("Glow",self.__repr__(),f"x: {x} y: {y} ")
        print("Glow",nameof(self),f"x: {x} y: {y} ")
        self.fillcolor("red")
        
    def unglow(self, x, y):
        print("unglow",self.__repr__(),f"x: {x} y: {y} ")
        self.fillcolor("")

    def set_robot_pose(self, x : float, y : float , theta : float):
        self.setpos(x ,y)
        self.setheading(theta)

        
    def move_and_collide():
        Yarp.yarp_time += 0.5
        # bail if the robot is out of the screen
        if (rob1.xcor() > turtle.screensize()[0]//2 or rob1.xcor() < -turtle.screensize()[0]//2 or 
            rob1.ycor() > turtle.screensize()[1]//2 or rob1.ycor() < -turtle.screensize()[1]//2 or
            rob2.xcor() > turtle.screensize()[0]//2 or rob2.xcor() < -turtle.screensize()[0]//2 or 
            rob2.ycor() > turtle.screensize()[1]//2 or rob2.ycor() < -turtle.screensize()[1]//2):
            
            print("Out of Bounds!", rob1.pos())
            print("Scr Size", turtle.Screen().screensize())
            Yarp.byebye()

        # check if the robots collided           
        if math.dist(rob1.pos(),rob2.pos())<40:
            print("Robots collided!")
            Yarp.byebye()

        # Execute robot's movement
        rob1.left(rob1.omega/2)
        rob1.forward(rob1.vel/2)
        rob1.left(rob1.omega/2)
        rob1.forward(rob1.vel/2)

        rob2.left(rob2.omega/2)
        rob2.forward(rob2.vel/2)
        rob2.left(rob2.omega/2)
        rob2.forward(rob2.vel/2)

        rob1.vel+=1
        rob2.vel+=2
        rob1.omega+=random.randrange(-10,10)
        rob2.omega+=random.randrange(-5,int(rob2.vel//4))
        
        # rob1.set_robot_pose(rob1.pos()[0], rob1.pos()[1], rob1.heading())
        
        if (int(Yarp.yarp_time*2) % 5 == 0):
            print ("Rob1 pose: ", rob1.pos(), rob1.heading(), "R1_vels=", rob1.vel, rob1.omega)
            print ("Rob2 pose: ", rob2.pos(), rob2.heading(), "R2_vels=", rob2.vel, rob2.omega)
        
        turtle.ontimer(Yarp.move_and_collide, 500)
        
   
# Start of main code

#turtle.Screen().setup(800,600)
turtle.Screen().screensize( canvwidth=800, canvheight=600 ) # not working ??
time.sleep(0.1)
print("Scr Size", turtle.Screen().screensize())
turtle.title("YARP - Yet Another Robot in Python (python turtle)")
turtle.bgcolor("lightgrey") # https://www.webucator.com/article/python-color-constants-module/
turtle.bgpic("logo.png") 

MyDraw.draw_quad(Point2D(-200,200), Point2D(200,200), Point2D(200,-200), Point2D(-200,-200), "orange")

# Create two robots
rob1 = Yarp()
rob2 = Yarp()
rob2.shape("triangle")
rob2.color("green")
rob2.fillcolor("")
rob2.penup()
rob2.goto(100,100)
rob2.pendown()

if False: # Test code for turtle healthiness of coordinates
    def exit_program():
        exit()
    time.sleep(0.1)
    rob1.setpos(0,0)
    rob1.setheading(0)
    rob1.forward(100)
    rob1.write_pos()
    rob1.back(200)
    rob1.write_pos()
    time.sleep(0.1)
    rob1.setpos(0,0)
    rob1.setheading(45)
    rob1.forward(math.sqrt(2)*200)
    rob1.back(math.sqrt(2)*400)
    rob1.write_pos()
    time.sleep(0.1)
    rob2.setpos(0,0)
    rob2.setheading(-45)
    rob2.forward(math.sqrt(2)*200)
    rob2.back(math.sqrt(2)*400)
    rob2.write_pos()
    rob2.write("Press ESC again to exit", align="center", font = ("Courier", 24, "normal"))
    time.sleep(2)
    turtle.listen()
    turtle.onkeypress(exit_program, "Escape")
    turtle.mainloop()
    exit()
    

# Bind the arrow keys and other keys to the functions
turtle.listen()

#
# ~~~~~~ Start of Test line draw and intersection ~~~~~~
#

if False:            # Test line draw and intersection "Unit Test"
    random.seed(10)

    for i in range(6):
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

        MyDraw.draw_seg(p1,p2, col)
        MyDraw.draw_seg(p3,p4, col)

        p_lin_cross = l1.intersection(l2)
        p_seg_cross = s1.intersection(s2)
        
        if len(p_seg_cross)>0:
            MyDraw.draw_point(p_seg_cross+[5,5], col, 5)
            print("Segment Interception:", p_seg_cross[0].evalf())
        else:
            print("No Segment Interception")

        if len(p_lin_cross)>0:
            MyDraw.draw_point(p_lin_cross, col)
            print("Line Interception:", p_lin_cross[0].evalf())
            #print(f"Seg Dist: {s1.distance(p_lin_cross[0]):.2f}, {s2.distance(p_lin_cross[0])}")
            print("Seg1 Dist: {:.2f}".format(float(s1.distance(p_lin_cross[0]))))
            print("Seg2 Dist: {:.2f}".format(float(s2.distance(p_lin_cross[0]))))
        else:
            print("No Line Interception")

        time.sleep(0.5)
    exit()
        
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
    turtle.onscreenclick(rob1.place_robot_at, 1, True)

    # Transfer control to Tkinter process events
    turtle.mainloop()
    
        
   
  
# Fim Código principal



