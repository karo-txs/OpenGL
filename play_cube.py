
import pygame
from OpenGL.raw.GLU import gluPerspective
from pygame import DOUBLEBUF, OPENGL
from jupyter3D import rotate_cube

def scene():
    pygame.init()
    display = (1366, 768)
    window = pygame.display
    window.set_mode(display, DOUBLEBUF | OPENGL)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    while True:
        rotate_cube.start(window)
if __name__ == "__main__":
    scene()

