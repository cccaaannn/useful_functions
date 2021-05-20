import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np



from cube import cube

cubes = []
for _ in range(10):
    temp = []
    for _ in range(10):
        temp.append(cube())
    cubes.append(temp)


cordX = 0
cordY = 0
for i in range(10):
    for j in range(10):
        cubes[i][j].add_to_x(cordX)
        cubes[i][j].add_to_y(cordY)
        cordX += 2
    cordX = 0
    cordY += 2



# pygame setup
pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, 70.0)
glTranslatef(0.0, 0.0, -40)


# frame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotatef(1, 0, 1, 0)

    for i in range(10):
        for j in range(10):
            cubes[i][j].draw()

    pygame.display.flip()
    pygame.time.wait(10)

