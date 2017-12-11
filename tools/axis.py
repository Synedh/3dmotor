from OpenGL.GL import *


def axis():
    glLineWidth(2)
    glBegin(GL_LINES)
    glColor3f(1,0,0)
    glVertex3f(-1000,0,0)
    glVertex3f(1000,0,0)
    glColor3f(0,1,0)
    glVertex3f(0,-1000,0)
    glVertex3f(0,1000,0)
    glColor3f(0,0,1)
    glVertex3f(0,0,-1000)
    glVertex3f(0,0,1000)
    glEnd()

    glColor3f(1,1,1)
    glPointSize(10)
    glBegin(GL_POINTS)
    glVertex3f(0, 0, 0)
    glEnd()
