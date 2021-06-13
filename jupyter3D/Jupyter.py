from OpenGL.GL import *
from OpenGL.raw.GLU import GLUquadric, gluNewQuadric, gluSphere, gluDisk


class Jupyter:
    def draw_jupyter(self, x, y):

        glColor3f(230 / 255, 182 / 255, 126 / 255)
        GLUquadric * 1
        quad = gluNewQuadric()
        glTranslatef(x, y, 0)
        gluSphere(quad, 14, 200, 2000)

    def draw_jupyter_matrix(self, boxx, boxy):
        glPushMatrix()
        glTranslatef(0, 0, -55)
        glTranslatef(boxx, boxy, 0)
        self.draw_jupyter(0, 0)
        glPopMatrix()

