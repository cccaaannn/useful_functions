import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



def line():
    glBegin(GL_LINES)
    glVertex2f(1,1.5)
    glVertex2f(-1,1.5)
    glEnd()


def triangle():
    glBegin(GL_LINES)

    glVertex2f(1,1)
    glVertex2f(-1,1)

    glVertex2f(1,1)
    glVertex2f(1,-1)

    glVertex2f(-1,1)
    glVertex2f(1,-1)
    glEnd()


def triangle2():
    glBegin(GL_LINES)

    glVertex2f(1,1)
    glVertex2f(-1,1)

    glVertex2f(1,1)
    glVertex2f(0,0)

    glVertex2f(-1,1)
    glVertex2f(0,0)
    glEnd()




# square
corners = [
    [1,1],
    [1,-1],
    [-1,-1],
    [-1,1]
]

edges = [
    [0,1],
    [1,2],
    [2,3],
    [3,0]
]


# hexagon
# corners = [
#     [-1,2],
#     [-2,0],
#     [-1,-2],
#     [1,-2],
#     [2,0],
#     [1,2]
# ]

# edges = [
#     [0,1],
#     [1,2],
#     [2,3],
#     [3,4],
#     [4,5],
#     [5,0]
# ]



def draw2d():
    glBegin(GL_LINES)
    for edge in edges:
        for corner in edge:
            glVertex2fv(corners[corner]) # there is a v at the end of the function because we are pasing array ex:[0,1]
    glEnd()






# pygame setup
pygame.init()
display = (900, 700)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0,0.0, -5)


# frame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) # clear opengl buffer on every frame

    # drawing functions
    line()
    draw2d()


    # pygame.display.update()
    pygame.display.flip() # this has to be filp instead of update for opengl
    pygame.time.wait(10) # limit the frame rate


