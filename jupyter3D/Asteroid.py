from OpenGL.GL import *
from OpenGL.GLU import gluSphere
from OpenGL.GLU.quadrics import GLUquadric
from OpenGL.raw.GLU import gluNewQuadric


class Asteroid:
    def __init__(self):
        self.x = -1
        self.y = -1

    def draw_asteroid(self, x, y):
        glColor3f(0.75, 0.54, 0.33)
        GLUquadric * 1
        quad = gluNewQuadric()
        glTranslatef(x, y, -10)
        gluSphere(quad, 1, 100, 500)

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
