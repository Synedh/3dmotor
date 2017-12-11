import pygame
import pygame.locals as pl
import sys
from math import cos, sin
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from tools.camera import Camera
from tools.menu import createGLUTMenus
from tools.axis import axis
from objects.pyramid import pyramid

mouse_button_pressed = []
keys_pressed = {}
camera = Camera()
objects = [pyramid()]


def key_pressed(key, x, y):
    if key == b'\x1b':
        quit()
    print("Key pressed : {}, X : {}, Y: {}".format(key, x, y))
    keys_pressed[key] = True


def key_released(key, x, y):
    print("Key released : {}, X : {}, Y: {}".format(key, x, y))
    del keys_pressed[key]


def mouse_pressed(key, state, x, y):
    global mouse_button_pressed
    print("Key : {}, state : {}, X: {}, Y: {}".format(key, state, x, y))
    if state == GLUT_DOWN:
        mouse_button_pressed.append([key, x, y, x, y])
    else:
        mouse_button_pressed.pop(-1)


def mouse_move_while_pressed(x, y):
    width, height = glutGet(GLUT_WINDOW_WIDTH), glutGet(GLUT_WINDOW_HEIGHT)
    key = [mouse_button_pressed[-1][0], mouse_button_pressed[-1][3], mouse_button_pressed[-1][4], x, y]
    mouse_button_pressed[-1] = key
    if key[0] == 2:
        camera.lookAt(key[3] - key[1], key[4] - key[2])
    print('Key : {}'.format(mouse_button_pressed[-1]))


def reshape(width, height): # Called when window is reshaped
    if height <= 1:
        height == 1
    glMatrixMode(GL_PROJECTION) # Switch to the projection matrix so that we can manipulate how our scene is viewed  
    glLoadIdentity() # Reset the projection matrix to the identity matrix so that we don't get any artifacts (cleaning up)  
    glViewport(0, 0, width, height) # Set our viewport to the size of our window  
    gluPerspective(45, width / height, 1.0, 100.0) # Set the Field of view angle (in degrees), the aspect ratio of our window, and the new and far planes  
    glMatrixMode(GL_MODELVIEW) # Switch back to the model view matrix, so that we can start drawing shapes correctly.


def display(): # Called on each iteration
    # Clear the color and depth buffers
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    # Load camera
    camera.update(keys_pressed)
    camera.draw()
    camera.hud()

    # Load basics
    axis()

    # Load objects
    for obj in objects:
        obj.draw()

    glPointSize(10)
    glColor3f(1,1,1)
    glBegin(GL_POINTS)
    glVertex3f(camera.lx, camera.ly, camera.lz)
    glEnd()


    glPointSize(10)
    glColor3f(0,1,1)
    glBegin(GL_POINTS)
    glVertex3f(camera.x, camera.y, camera.z)
    glEnd()

    # Copy the off-screen buffer to the screen.
    glutSwapBuffers()

    # Force opengl to call display on each loop.
    glutPostRedisplay()


def main():
    glutInit(sys.argv)

    # Create a double-buffer RGBA window with depth calculation.
    glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

    # Create a window.
    glutInitWindowPosition(100,100)
    glutInitWindowSize(800, 800)
    glutCreateWindow('3D Motor')

    # Enable depth test.
    glEnable(GL_DEPTH_TEST)

    # Set display, reshape, keyboard and mouse callbacks.
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutKeyboardFunc(key_pressed)
    glutSpecialFunc(key_pressed)
    glutKeyboardUpFunc(key_released)
    glutSpecialUpFunc(key_released)
    glutMouseFunc(mouse_pressed)
    glutMotionFunc(mouse_move_while_pressed)

    # createGLUTMenus()

    glutIgnoreKeyRepeat(1)

    # Run the GLUT main loop until the user closes the window.
    glutMainLoop()


if __name__ == '__main__':
    main()
