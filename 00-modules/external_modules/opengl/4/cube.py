import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np


class cube():
    def __init__(self):
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

        self.colors = {
            "green":(0, 0.8, 0),
            "purple":(0.4, 0, 1)
            }

        self.corner_colors = {
            0:self.colors["green"],
            1:self.colors["purple"],
            2:self.colors["purple"],
            3:self.colors["green"],
            
            4:self.colors["green"],
            5:self.colors["purple"],
            6:self.colors["purple"],
            7:self.colors["green"]
        }


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



    def draw(self, draw_surface=False):
        # draws the cube, if selected with the surfaces

        if(draw_surface):
            glBegin(GL_QUADS)
            for surface in self.surfaces:
                for vertex in surface:
                    glColor3fv(self.corner_colors[vertex])
                    glVertex3fv(self.corners[vertex])
            glEnd()

        glBegin(GL_LINES)
        for edge in self.edges:
            for corner in edge:
                glColor3fv(self.corner_colors[corner])
                glVertex3dv(self.corners[corner])
        glEnd()

