from OpenGL.GLUT import *


def processMenuEvents(option):
    print('test ')


def createGLUTMenus():
    menu = glutCreateMenu(processMenuEvents)

    # add entries to our menu
    glutAddMenuEntry("Red", 0);
    glutAddMenuEntry("Blue", 1);
    glutAddMenuEntry("Green", 2);
    glutAddMenuEntry("Orange", 3);

    # attach the menu to the right button
    glutAttachMenu(GLUT_MIDDLE_BUTTON);
