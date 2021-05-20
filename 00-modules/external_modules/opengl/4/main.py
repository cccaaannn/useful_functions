import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np



from cube import cube

cube1 = cube()
cube1.change_size(5)

cube2 = cube()
cube2.add_to_x(5)

cube3 = cube()
cube3.add_to_x(-5)

cube4 = cube()
cube4.add_to_y(5)

cube5 = cube()
cube5.add_to_y(-5)

cube6 = cube()
cube6.add_to_z(5)

cube7 = cube()
cube7.add_to_z(-5)




# pygame setup
pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -15)


counter = 0
multiplier = 0.98
# frame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotatef(1, 0, 1, 0)

    # draw cubes
    cube1.draw()
    cube2.draw()
    cube3.draw()
    cube4.draw(draw_surface=True)
    cube5.draw(draw_surface=True)
    cube6.draw()
    cube7.draw()


    # change the size multiplier
    counter += 1
    if(counter == 100):
        multiplier = 1.02        
    elif(counter == 200):
        multiplier = 0.98
        counter = 0


    cube1.change_size(multiplier)

    # to change the size of an object that is not on the origin
    # move it to origin first, resize and move it back
    cube2.add_to_x(-5)
    cube2.change_size(multiplier)
    cube2.add_to_x(5)



    pygame.display.flip()
    pygame.time.wait(10)








