import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


class cube():
    def __init__(self, texture_path):
        self.corners = np.array(
            [[ 0.5, 0.5,  0.5],
            [ 0.5, -0.5,  0.5],
            [-0.5,  -0.5,  0.5],
            [-0.5, 0.5,  0.5],
            [ 0.5,  0.5, -0.5],
            [ 0.5, -0.5, -0.5],
            [-0.5,  -0.5, -0.5],
            [-0.5, 0.5, -0.5]]
            )

        self.edges = np.array(
            [[0,1],
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
            [3,7]]
            )

        self.surfaces = np.array(
            [[0,1,2,3],
            [4,5,6,7],

            [0,3,7,4],
            [1,2,6,5],

            [0,1,5,4],
            [2,3,7,6]]
            )

        self.texture_coords = np.array(
            [[1,0],
            [1,1],
            [0,1],
            [0,0]]
            )

        # load texture
        self.load_texture(texture_path)


    # change location
    def add_to_x(self, num):
        self.corners = np.column_stack((self.corners[:,0]+num, self.corners[:,1], self.corners[:,2]))

    def add_to_y(self, num):
        self.corners = np.column_stack((self.corners[:,0], self.corners[:,1]+num, self.corners[:,2]))

    def add_to_z(self, num):
        self.corners = np.column_stack((self.corners[:,0], self.corners[:,1], self.corners[:,2]+num))


    # change size
    def change_size(self, size):
        self.corners = self.corners * size



    def load_texture(self, texture_path):
        # load texture with pygame
        tex = pygame.image.load(texture_path)
        tex_surface = pygame.image.tostring(tex, 'RGBA')
        tex_width, tex_height = tex.get_size()

        # generate texture id and bind it to that id
        self.texture_id = glGenTextures(1)    
        glBindTexture(GL_TEXTURE_2D, self.texture_id)

        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, tex_width, tex_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, tex_surface)

        glBindTexture(GL_TEXTURE_2D, 0)


    def check_Collision(self, cube):
        # https://www.cbcity.de/simple-3d-collision-detection-with-python-scripting-in-blender

        x_max = max([e[0] for e in self.corners])
        x_min = min([e[0] for e in self.corners])
        y_max = max([e[1] for e in self.corners])
        y_min = min([e[1] for e in self.corners])
        z_max = max([e[2] for e in self.corners])
        z_min = min([e[2] for e in self.corners])
        # print('Box1 min %.2f, %.2f, %.2f' % (x_min, y_min, z_min))
        # print('Box1 max %.2f, %.2f, %.2f' % (x_max, y_max, z_max))
        
        x_max2 = max([e[0] for e in cube.corners])
        x_min2 = min([e[0] for e in cube.corners])
        y_max2 = max([e[1] for e in cube.corners])
        y_min2 = min([e[1] for e in cube.corners])
        z_max2 = max([e[2] for e in cube.corners])
        z_min2 = min([e[2] for e in cube.corners])
        # print('Box2 min %.2f, %.2f, %.2f' % (x_min2, y_min2, z_min2))
        # print('Box2 max %.2f, %.2f, %.2f' % (x_max2, y_max2, z_max2))

        isColliding = ((x_max > x_min2 and x_min < x_max2) and (y_max > y_min2 and y_min < y_max2) and (z_max > z_min2 and z_min < z_max2))

        return isColliding


    def get_largest_abs_cord(self):
        # check the largest coordinate to delete cubes that are far away
        return np.abs(self.corners).max()

    def set_acceleration_cords(self, x, y, z):
        # sets acceleration coordinates ahead of time
        self.directionX = x
        self.directionY = y
        self.directionZ = z

    def accelerate_cube(self, acceleration):
        # accelerates the cube to the selected direction
        self.add_to_x(acceleration*self.directionX)
        self.add_to_y(acceleration*self.directionY)
        self.add_to_z(acceleration*self.directionZ)


    def draw(self):
        # draws the cube with texture
        glBindTexture(GL_TEXTURE_2D, self.texture_id)
        glBegin(GL_QUADS)
        for surface in self.surfaces:
            for index, vertex in enumerate(surface):
                glTexCoord2dv(self.texture_coords[index])
                glVertex3fv(self.corners[vertex])
        glEnd()
        glBindTexture(GL_TEXTURE_2D, 0)

