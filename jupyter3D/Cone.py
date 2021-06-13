import math
from OpenGL.GL import *
from OpenGL.GLU import gluCylinder

from OpenGL.GLU.quadrics import GLUquadric
from OpenGL.raw.GLU import gluNewQuadric


class Cone:
    def __init__(self):
        self.x = -1
        self.y = -1

    def draw_cone(self, x, y, tam):
        glColor3f(0.76, 1, 0.13)
        GLUquadric * 1
        quad = gluNewQuadric()
        glTranslatef(x, y, 0)
        gluCylinder(quad, 2, 0.1, 2, 50, 50)

        glTranslatef(-20, -20, 0)
        gluCylinder(quad, 0.1, 2, 3, 50, 50)

    def draw_cone_matrix(self, x, y, tam):
        if self.x == -1 and self.y == -1:
            self.x = x
            self.y = y

        glPushMatrix()
        glTranslatef(0, 0, -tam)

        self.x -= 0.3
        glTranslatef(self.x, 0, 0)
        self.draw_cone(self.x, self.y, tam)
        glPopMatrix()

    def draw_cone_scalef(self, x, y, tam):
        if self.x == -1 and self.y == -1:
            self.x = x
            self.y = y

        glPushMatrix()
        #glTranslatef(0, 0, -tam)

        self.x -= 0.3
        #glTranslatef(self.x, 0, 0)
        glScalef(10, 10, 10)
        self.draw_cone(self.x, self.y, tam)
        glPopMatrix()