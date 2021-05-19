import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


def load_texture(texture_url):
    # load texture with pygame
    tex = pygame.image.load(texture_url)
    tex_surface = pygame.image.tostring(tex, 'RGBA')
    tex_width, tex_height = tex.get_size()

    # generate texture id and bind it to that id
    tex_id = glGenTextures(1)    
    glBindTexture(GL_TEXTURE_2D, tex_id)

    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, tex_width, tex_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, tex_surface)

    glBindTexture(GL_TEXTURE_2D, 0)
    return tex_id


def square(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)

    glTexCoord(1, 0)        # top right
    glVertex3d(1,1,1)
    glTexCoord(1,1)         # bottom right
    glVertex3d(1,-1,1)
    glTexCoord(0, 1)        # bottom left
    glVertex3d(-1,-1,1)
    glTexCoord(0, 0)        # top left
    glVertex3d(-1,1,1)

    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)



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

texture_coords = [
    [1,0],
    [1,1],
    [0,1],
    [0,0]
]

def cube(texture):
    glBindTexture(GL_TEXTURE_2D, texture)
    glBegin(GL_QUADS)
    for surface in surfaces:
        for index, corner in enumerate(surface):
            glTexCoord2dv(texture_coords[index])
            glVertex3dv(corners[corner])
    glEnd()
    glBindTexture(GL_TEXTURE_2D, 0)




# pygame setup
pygame.init()
display = (800,600)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
glTranslatef(0.0, 0.0, -5)

# enable texture
glEnable(GL_TEXTURE_2D)
glEnable(GL_DEPTH_TEST)


# load texture
texture = load_texture("3/texture.jpg")

# frame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glRotatef(1, 1, 1, 1)
    cube(texture)

    pygame.display.flip()
    pygame.time.wait(10)

