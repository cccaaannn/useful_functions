import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *



corners = (
    # 0 1
    (1, 1, 1),
    (1, -1, 1),

    # 2 3
    (-1, 1, 1),
    (-1, -1, 1),

    # 4 5
    (1, 1, -1),
    (1, -1, -1),
    
    # 6 7
    (-1, 1, -1),
    (-1, -1, -1)
)


edges = (

    # cube
    (0,1),
    (2,3),
    (0,2),
    (1,3),

    (4,5),
    (6,7),
    (4,6),
    (5,7),

    (0,4),
    (1,5),
    (2,6),
    (3,7),

    # (3,4),
    # (0,7)
)


surfaces = (
    (0,1,3,2),
    (4,5,7,6),
    (0,2,6,4),
    (1,3,7,5),
    (0,1,5,4),
    (2,3,7,6)
)


def cube_fill_color():
    # we are drawing quads
    glBegin(GL_QUADS)

    for surface in surfaces:
        for vertex in surface:
            if(vertex % 2 == 0):
                glColor3fv((0,1,0))
            else:
                glColor3fv((0,0,1))

            glVertex3fv(corners[vertex])
    glEnd()

    glBegin(GL_LINES)
    glColor3fv((1,0,0))
    for edge in edges:
        for vertex in edge:
            glVertex3fv(corners[vertex])
    glEnd()





# pygame setup
pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)


# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -40)






def game():
    object_passed = False
    movement_speed = 0.3
    cube_speed = 0.1

    # frame loop
    while not object_passed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(movement_speed,0,0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(-movement_speed,0,0)
                if event.key == pygame.K_UP:
                    glTranslatef(0,-movement_speed,0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0,movement_speed,0)


        glTranslatef(0,0,cube_speed)


        x = glGetDoublev(GL_MODELVIEW_MATRIX)
        # print(x)

        camera_x = x[3][0]
        camera_y = x[3][1]
        camera_z = x[3][2]


        if(camera_z < -1):
            object_passed = True
            print("asdasd")




        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        cube_fill_color()

        pygame.display.flip()
        pygame.time.wait(10)



game()
pygame.quit()
quit()








