"""
Aum Desai
Fall 2022
CS152B Final Project

This program calculates and makes the 3-D graphics for the molecules. 
"""


from graphicsPlus import *
import math
import time

def main(balls,sticks,text):


    class Sphere(Circle):
        def __init__(self,dist,dist2,dist3,atom):

            '''
            This method initilizes the class object of spheres with 4 additional attributes.
            '''

            self.x = 250
            self.y = 250

            if atom == 1:

                self.scale = 20
                self.color = 'yellow'

            elif atom == 2:

                self.scale = 10
                self.color = 'red'

            elif atom == 3:

                self.scale = 20
                self.color = 'green'

            else:

                self.scale = 20
                self.color = 'blue'

            self.dist = dist
            self.dist2 = dist2
            self.dist3 = dist3
            self.ang = 180
            self.ang2 = 180
            self.ang3 = 180
            self.sphere = Circle(Point(0,0),1)

        def rot_x(self,dir):

            '''
            This method changes the internal angle of the sphere objects for calculations. For x
            '''

            self.ang += dir


        def rot_y(self,dir):

            '''
            This method changes the internal angle of the sphere objects for calculations. For y
            '''

            self.ang2 += dir

        def find_closeness(self):

            '''
            This method calculates where the sphere objects are on the z-axis for drawing purposes. 
            '''

            return ((1.3)**(math.sin(math.radians(self.ang-90))*(self.dist)))*((1.3)**(math.sin(math.radians(self.ang2-90))*(self.dist2)))*((1.3)**(math.sin(math.radians(self.ang+self.ang2+90))*(self.dist3)))

        def new_frame(self):

            '''
            This method undraws the current sphere and calculates where the new sphere should be drawn basd on the x and y rotation.
            '''

            self.sphere.undraw()
            self.sphere = Circle(Point(self.x+math.sin(math.radians(self.ang))*self.dist+math.sin(math.radians(self.ang-self.ang3+90))*self.dist3,self.y+math.sin(math.radians(self.ang2))*self.dist2+math.sin(math.radians(self.ang2-self.ang3+90))*self.dist3),self.scale*((1.1)**(math.sin(math.radians(self.ang-90))*(self.dist/60)))*((1.1)**(math.sin(math.radians(self.ang2-90))*(self.dist2/60)))*((1.1)**(math.sin(math.radians(self.ang+self.ang2+90))*(self.dist3/60))))

            self.sphere.setFill(self.color)
            return(self.sphere)

    spheres = []
    lines = []
    all_lines = []
    temp_lines = []

    balls = balls.split(",")

    for i in range(len(balls)):

        balls[i] = balls[i].split(" ")

    for i in balls:

        spheres.append(Sphere(int(i[0]),int(i[1]),int(i[2]),int(i[3])))

    sticks = sticks.split(",")

    for i in range(len(sticks)):

        sticks[i] = sticks[i].split(" ")

    for i in sticks:

        lines.append((int(i[0]),int(i[1])))

        all_lines.append(Line(Point(0,0),Point(0,0)))
        

    win = GraphWin(text, 500, 500)


    while True:

        curr_key = win.getKey()

        if curr_key == "b":

            break

        for a in range(90):

            time.sleep(0.01)

            if curr_key == "Up":

                for i in spheres:

                    i.rot_y(1)

            elif curr_key == "Down":

                for i in spheres:

                    i.rot_y(-1)

            elif curr_key == "Left":

                for i in spheres:

                    i.rot_x(-1)

            elif curr_key == "Right":

                for i in spheres:

                    i.rot_x(1)

            if curr_key == "Up" or curr_key == "Down" or curr_key == "Left" or curr_key == "Right":

                list_of_objs = []

                input_list = []

                temp_lines = lines.copy()

                for i in spheres:

                    input_list.append(i.find_closeness())

                indexed_list = [(input_list[i], i) for i in range(len(input_list))]

                sorted_indexed_list = sorted(indexed_list)

                sorted_initial_indexes = [t[1] for t in sorted_indexed_list]

                for i in sorted_initial_indexes:

                    list_of_objs.append(spheres[i].new_frame())

                    for j in range(len(temp_lines)):

                        if i in temp_lines[j]:

                            list_of_objs.append(Line(spheres[temp_lines[j][0]].sphere.getCenter(),spheres[temp_lines[j][1]].sphere.getCenter()))
                            list_of_objs[-1].setWidth(5)
                            temp_lines[j] = (-1,-1)

                for j in all_lines:
                    j.undraw()

                for i in list_of_objs:
                    i.draw(win)
                
                all_lines = list_of_objs[::-1]