import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


# cube
corners = [
    [1,1,1],
    [1,-1,1],
    [-1,-1,1],
    [-1,1,1],

    [1,1,-1],
    [1,-1,-1],
    [-1,-1,-1],
    [-1,1,-1]
]

edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,0],

    [4,5],
    [5,6],
    [6,7],
    [7,4],

    [0,4],
    [1,5],
    [2,6],
    [3,7],

    [0,6] # inner diagonal
]


# pyramid
# corners = [
#     [1,-1,1],
#     [-1,-1,1],
#     [-1,-1,-1],
#     [1,-1,-1],

#     [0,1,0]
# ]

# edges = [
#     [0,1],
#     [1,2],
#     [2,3],
#     [3,0],

#     [0,4],
#     [1,4],
#     [2,4],
#     [3,4]
# ]



# regular draw3d function
def draw3d():
    glBegin(GL_LINES)
    for edge in edges:
        for corner in edge:
            glVertex3fv(corners[corner])
    glEnd()



# color functions
def color1():
    glBegin(GL_LINES)
    # glColor3f(0,0,1) # color float version accepts values between 0 and 1
    # glColor3ub(255,0,0) # this one accepts between 0 - 255
    glColor4f(0,0,1,0.5) # color with alfa chanel (you also have to enable blending for this, check line 133)

    for edge in edges:
        for corner in edge:
            glVertex3fv(corners[corner])
    glEnd()



# color edges 
def color2():
    glBegin(GL_LINES)
    glColor3f(0,0,1)

    for index, edge in enumerate(edges):
        # make the diagonal green (this not works with pyramid since it doesn't have 12 edges)
        if(index == 12): 
            glColor3f(0,1,0)

        for corner in edge:
            glVertex3fv(corners[corner])
    glEnd()



# color corners
def color3():
    glBegin(GL_LINES)
    for edge in edges:
        for corner in edge:
            # make half of the corners blue 
            if(corner % 2 == 0):
                glColor3f(0,0,1)
            else:
                glColor3f(0,1,0)
            
            glVertex3fv(corners[corner])
    glEnd()





# pygame setup
pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)


# for alpha chanel
glEnable(GL_BLEND)
glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


# rotation
# glRotatef(45,0,1,0)


# frame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotatef(1,0,1,0) # continuous rotation
    color3()

    pygame.display.flip()
    pygame.time.wait(10)

