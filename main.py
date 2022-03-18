from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import numpy as np
from PIL import Image
from OpenGL.GL.shaders import *

import sys, os

global img
global img_arr
global Width
global Height
global vertexVBO
vertexVBO = glGenFramebuffers(1)

img = Image.open(os.path.abspath(os.curdir)+'/imgs/2.jpg').rotate(0)
img_arr = np.array(
    img.getdata(),
    np.uint8
)
Width, Height = img.size


def load_shaders():
    global vertex
    with open('glsl/vertex.glsl', 'r') as f:
        vertex = f.read()

    # global fragment
    # with open('glsl/fragmentRGB2YIQ.glsl', 'r') as f:
    #     fragment = f.read()

    # global fragment1
    # with open('glsl/fragment.glsl', 'r') as f:
    #     fragment1 = f.read()

    global fragment
    with open('glsl/prewitt.glsl', 'r') as f:
        fragment = f.read()
    
    vertex = ''.join(vertex)
    fragment = ''.join(fragment)
    # fragment1 = ''.join(fragment1)


def init():
    # createBuffer

    # glBindFramebuffer(GL_FRAMEBUFFER, vertexVBO)

    # texture = glGenTextures(1)
    # glBindTexture(GL_TEXTURE_2D, texture)
    # glTexImage2D(
    #     GL_TEXTURE_2D,
    #     0,
    #     GL_RGB,
    #     Width,
    #     Height,
    #     0,
    #     GL_RGBA,
    #     GL_UNSIGNED_BYTE,
    #     None
    # )
    # glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST )
    # glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST )
    # glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE )
    # glTexParameteri( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE )

    # glFramebufferTexture2D(GL_FRAMEBUFFER, GL_COLOR_ATTACHMENT0, GL_TEXTURE_2D, texture, 0)

    # endBuffer
    glClearColor(0.7, 1.0, 0.7, 1)

    glBindTexture(GL_TEXTURE_2D, 0)

    gluBuild2DMipmaps(
        GL_TEXTURE_2D,
        3,
        Width,
        Height,
        GL_RGB,
        GL_UNSIGNED_BYTE,
        np.array(
            img.getdata(),
            np.uint8
        )
    )
    
    #Set Camera Matrix parameters
    glMatrixMode(GL_PROJECTION)
    gluPerspective(90.0, Width/Height, 0.1, 50.0)
    
    #set ModelView Matrix parameters
    glMatrixMode(GL_MODELVIEW)

    

    vertex_shader = compileShader(vertex, GL_VERTEX_SHADER)
    fragment_shader = compileShader(fragment, GL_FRAGMENT_SHADER)
    # fragment_shader1 = compileShader(fragment1, GL_FRAGMENT_SHADER)

    global program
    program = compileProgram(vertex_shader, fragment_shader)
    # global program1
    # program1 = compileProgram(vertex_shader, fragment_shader1)

    

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Restore Model Matrix parameters
    glLoadIdentity()
    
    # Translate
    glTranslatef(0, 0, -6)
    
    # Load OpenGL(with shaders)program context 
    # glBindBuffer(GL_TEXTURE_2D, )
    glUseProgram(program)
    # glUseProgram(program1)

    #Texture                
    
    glEnable(GL_TEXTURE_2D)
    #Draw Quad-points with associated texture coordinates
    
    glBegin(GL_QUADS)

    glTexCoord2d(1,1)   # правый верхний
    glVertex2d(-5,-5)    # левый нижний

    glTexCoord2d(0,1)   # левый верхний
    glVertex2d( 5, -5)  # правый нижний
    
    glTexCoord2d(0,0)   # левый нижний
    glVertex2d( 5, 5)   # правый верхний

    glTexCoord2d(1,0)    # правый нижний
    glVertex2d( -5, 5)  # левый верхний
    
    glEnd()
    
    #Load parameters to fragment shader
    glUniform1i( glGetUniformLocation( program, "s_texture" ), 0 )
    glUniform1f( glGetUniformLocation( program, "texture_width" ), float( img.size[ 0 ] ) )
    glUniform1f( glGetUniformLocation( program, "texture_height" ), float( img.size[ 1 ] ) )
    
    glFlush()


def main():
    load_shaders()
    glutInit("Glut")
    glutInitWindowSize(Width*3,Height*3)
    glutCreateWindow('Window')

    glutDisplayFunc(draw)
    # print(list(img.getdata()))
    init()
    
    glutMainLoop()
    

if __name__ == '__main__':
    main()