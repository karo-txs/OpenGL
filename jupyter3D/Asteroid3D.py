import math
from OpenGL.GL import *
from OpenGL.GLU import gluSphere
from OpenGL.GLU.quadrics import GLUquadric
from OpenGL.raw.GLU import gluNewQuadric


class Asteroid3D:
    def __init__(self):
        self.x = -1
        self.y = -1

    def draw_asteroid(self, x, y):

        glColor3f(1, 0.76, 0.13 );
        quad = gluNewQuadric();
        glTranslatef(x, y, 0);
        gluSphere(quad, 2, 30, 30);

    def draw_asteroid_matrix(self, x, y, tam):
        if self.x == -1 and self.y == -1:
            self.x = x
            self.y = y

        glPushMatrix()
        glTranslatef(0, 0, -tam)

        self.x -= 0.3
        glTranslatef(self.x, 0, 0)
        self.draw_asteroid(self.x, self.y)
        glPopMatrix()