from OpenGL.GL import *


class Garbage:
    def __init__(self):
        self.x = -1
        self.y = -1
        self.z = -1

    def draw_garbage2(self, x, y, z):
        glRotatef(90, 1.0, 0.0, 0.0)

        # FRENTE
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(5 + x, -1 + y, -1 + z)
        glVertex3f(5 + x, 1 + y, -1 + z)
        glVertex3f(-5 + x, 1 + y, -1 + z)
        glVertex3f(-5 + x, -1 + y, -1 + z)
        glEnd()

        # TRASEIRA
        glBegin(GL_POLYGON)
        glColor3f(0.3, 0.3, 0.3)
        glVertex3f(5 + x, -1 + y, 1 + z)
        glVertex3f(5 + x, 1 + y, 1 + z)
        glVertex3f(-5 + x, 1 + y, 1 + z)
        glVertex3f(-5 + x, -1 + y, 1 + z)
        glEnd()

        # DIREITA
        glBegin(GL_POLYGON)
        glColor3f(0.3, 0.3, 0.3)
        glVertex3f(5 + x, -1 + y, -1 + z)
        glVertex3f(5 + x, 1 + y, -1 + z)
        glVertex3f(5 + x, 1 + y, 1 + z)
        glVertex3f(5 + x, -1 + y, 1 + z)
        glEnd()

        # ESQUERDA
        glBegin(GL_POLYGON)
        glColor3f(0.7, 0.7, 0.7)
        glVertex3f(-5 + x, -1 + y, 1 + z)
        glVertex3f(-5 + x, 1 + y, 1 + z)
        glVertex3f(-5 + x, 1 + y, -1 + z)
        glVertex3f(-5 + x, -1 + y, -1 + z)
        glEnd()

        # TOPO
        glBegin(GL_POLYGON)
        glColor3f(0.7, 0.7, 0.7)
        glVertex3f(5 + x, 1 + y, 1 + z)
        glVertex3f(5 + x, 1 + y, -1 + z)
        glVertex3f(-5 + x, 1 + y, -1 + z)
        glVertex3f(-5 + x, 1 + y, 1 + z)
        glEnd()

        # BASE
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(5 + x, -1 + y, -1 + z)
        glVertex3f(5 + x, -1 + y, 1 + z)
        glVertex3f(-5 + x, -1 + y, 1 + z)
        glVertex3f(-5 + x, -1 + y, -1 + z)
        glEnd()

    def draw_garbage(self, x, y, z):
        glLoadIdentity()
        glRotatef(120, 1.0, 0.0, 0.0)

        # FRENTE
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(2 + x, -2 + y, -2 + z)
        glVertex3f(2 + x, 2 + y, -2 + z)
        glVertex3f(-2 + x, 2 + y, -2 + z)
        glVertex3f(-2 + x, -2 + y, -2 + z)
        glEnd()

        # TRASEIRA
        glBegin(GL_POLYGON)
        glColor3f(0.3, 0.3, 0.3)
        glVertex3f(2 + x, -2 + y, 2 + z)
        glVertex3f(2 + x, 2 + y, 2 + z)
        glVertex3f(-2 + x, 2 + y, 2 + z)
        glVertex3f(-2 + x, -2 + y, 2 + z)
        glEnd()

        # DIREITA
        glBegin(GL_POLYGON)
        glColor3f(0.3, 0.3, 0.3)
        glVertex3f(2 + x, -2 + y, -2 + z)
        glVertex3f(2 + x, 2 + y, -2 + z)
        glVertex3f(2 + x, 2 + y, 2 + z)
        glVertex3f(2 + x, -2 + y, 2 + z)
        glEnd()

        # ESQUERDA
        glBegin(GL_POLYGON)
        glColor3f(0.7, 0.7, 0.7)
        glVertex3f(-2 + x, -2 + y, 2 + z)
        glVertex3f(-2 + x, 2 + y, 2 + z)
        glVertex3f(-2 + x, 2 + y, -2 + z)
        glVertex3f(-2 + x, -2 + y, -2 + z)
        glEnd()

        # TOPO
        glBegin(GL_POLYGON)
        glColor3f(0.7, 0.7, 0.7)
        glVertex3f(2 + x, 2 + y, 2 + z)
        glVertex3f(2 + x, 2 + y, -2 + z)
        glVertex3f(-2 + x, 2 + y, -2 + z)
        glVertex3f(-2 + x, 2 + y, 2 + z)
        glEnd()

        # BASE
        glBegin(GL_POLYGON)
        glColor3f(0.5, 0.5, 0.5)
        glVertex3f(2 + x, -2 + y, -2 + z)
        glVertex3f(2 + x, -2 + y, 2 + z)
        glVertex3f(-2 + x, -2 + y, 2 + z)
        glVertex3f(-2 + x, -2 + y, -2 + z)
        glEnd()

    def draw_garbage_matrix(self, x, y, z, tam):
        if self.x == -1 and self.y == -1:
            self.x = x
            self.y = y
            self.z = z

        glPushMatrix()
        self.x -= 0.3
        glLoadIdentity()
        glTranslatef(self.x, 0, tam)
        self.draw_garbage(self.x, y, z)

        self.x -= 0.3
        glLoadIdentity()

        glTranslatef(self.x + 50, 150, tam)
        self.draw_garbage2(self.x - 80, y - 200, z - 60)
        glPopMatrix()
