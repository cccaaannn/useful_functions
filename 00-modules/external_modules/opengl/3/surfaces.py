import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



def triangle():
    glBegin(GL_TRIANGLES)
    glColor3f(0,0,1)
    glVertex3f(0,1,0)
    glVertex3f(-1,-1,0)    
    glVertex3f(1,-1,0)
    glEnd()

def square():
    glBegin(GL_QUADS)
    glVertex3f(1,1,0)
    glVertex3f(1,-1,0)
    glVertex3f(-1,-1,0)
    glVertex3f(-1,1,0)
    glEnd()



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

surfaces = [
    [0,1,2,3],
    [4,5,6,7],

    [0,3,7,4],
    [1,2,6,5],

    [0,1,5,4],
    [2,3,7,6]
]

def cube():
    glBegin(GL_QUADS)
    for surface in surfaces:
        for corner in surface:
            if(corner % 2 == 0):
                glColor3f(0,0,1)
            else:
                glColor3f(0,1,0)
            glVertex3fv(corners[corner])
    glEnd()



# pyramid
corners = [
    [1,-1,1],
    [-1,-1,1],
    [-1,-1,-1],
    [1,-1,-1],

    [0,1,0]
]

triangles = [
    [0,1,4],
    [1,2,4],
    [2,3,4],
    [3,0,4]
]

quads = [
    [0,1,2,3]
]

edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,0],

    [0,4],
    [1,4],
    [2,4],
    [3,4]
]

def pyramid():
    # bottom
    glBegin(GL_QUADS)
    for surface in quads:
        for corner in surface:
            glVertex3fv(corners[corner])
    glEnd()
    
    # sides
    glBegin(GL_TRIANGLES)
    for surface in triangles:
        for corner in surface:
            if(corner % 2 == 0):
                glColor3f(0,0,1)
            else:
                glColor3f(1,1,0)
            glVertex3fv(corners[corner])
    glEnd()

    # outer shell
    glBegin(GL_LINES)
    glColor3f(0,1,0)
    for edge in edges:
        for corner in edge:
            glVertex3fv(corners[corner])
    glEnd()



# hexagon
corners = [
    [-1,2,0],
    [-2,0,0],
    [-1,-2,0],
    [1,-2,0],
    [2,0,0],
    [1,2,0],

    [0,0,0] # canter
]

triangles = [
    [0,1,6],
    [1,2,6],
    [2,3,6],
    [3,4,6],
    [4,5,6],
    [5,0,6]
]

def hexagon():
    glBegin(GL_TRIANGLES)
    for index, triangle in enumerate(triangles):
        if(index % 2 == 0):
            glColor3f(0,0,1)
        else:
            glColor3f(0,1,0)
        for corner in triangle:
            glVertex3fv(corners[corner])
    glEnd()





# pygame setup
pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# disable interior visibility
# glEnable(GL_DEPTH_TEST)

# frame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


    glRotatef(1, 0, 1, 0)
    hexagon()


    pygame.display.flip()
    pygame.time.wait(10)

