import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from cube import cube



def InverseMat44(mat):
    # https://stackoverflow.com/questions/56641857/how-to-get-current-camera-position-in-pyopengl

    m = [mat[i][j] for i in range(4) for j in range(4)]
    inv = [0]*16

    inv[0]  =  m[5] * m[10] * m[15] - m[5] * m[11] * m[14] - m[9] * m[6] * m[15] + m[9] * m[7] * m[14] + m[13] * m[6] * m[11] - m[13] * m[7] * m[10]
    inv[4]  = -m[4] * m[10] * m[15] + m[4] * m[11] * m[14] + m[8] * m[6] * m[15] - m[8] * m[7] * m[14] - m[12] * m[6] * m[11] + m[12] * m[7] * m[10]
    inv[8]  =  m[4] * m[9]  * m[15] - m[4] * m[11] * m[13] - m[8] * m[5] * m[15] + m[8] * m[7] * m[13] + m[12] * m[5] * m[11] - m[12] * m[7] * m[9]
    inv[12] = -m[4] * m[9]  * m[14] + m[4] * m[10] * m[13] + m[8] * m[5] * m[14] - m[8] * m[6] * m[13] - m[12] * m[5] * m[10] + m[12] * m[6] * m[9]
    inv[1]  = -m[1] * m[10] * m[15] + m[1] * m[11] * m[14] + m[9] * m[2] * m[15] - m[9] * m[3] * m[14] - m[13] * m[2] * m[11] + m[13] * m[3] * m[10]
    inv[5]  =  m[0] * m[10] * m[15] - m[0] * m[11] * m[14] - m[8] * m[2] * m[15] + m[8] * m[3] * m[14] + m[12] * m[2] * m[11] - m[12] * m[3] * m[10]
    inv[9]  = -m[0] * m[9]  * m[15] + m[0] * m[11] * m[13] + m[8] * m[1] * m[15] - m[8] * m[3] * m[13] - m[12] * m[1] * m[11] + m[12] * m[3] * m[9]
    inv[13] =  m[0] * m[9]  * m[14] - m[0] * m[10] * m[13] - m[8] * m[1] * m[14] + m[8] * m[2] * m[13] + m[12] * m[1] * m[10] - m[12] * m[2] * m[9]
    inv[2]  =  m[1] * m[6]  * m[15] - m[1] * m[7]  * m[14] - m[5] * m[2] * m[15] + m[5] * m[3] * m[14] + m[13] * m[2] * m[7]  - m[13] * m[3] * m[6]
    inv[6]  = -m[0] * m[6]  * m[15] + m[0] * m[7]  * m[14] + m[4] * m[2] * m[15] - m[4] * m[3] * m[14] - m[12] * m[2] * m[7]  + m[12] * m[3] * m[6]
    inv[10] =  m[0] * m[5]  * m[15] - m[0] * m[7]  * m[13] - m[4] * m[1] * m[15] + m[4] * m[3] * m[13] + m[12] * m[1] * m[7]  - m[12] * m[3] * m[5]
    inv[14] = -m[0] * m[5]  * m[14] + m[0] * m[6]  * m[13] + m[4] * m[1] * m[14] - m[4] * m[2] * m[13] - m[12] * m[1] * m[6]  + m[12] * m[2] * m[5]
    inv[3]  = -m[1] * m[6]  * m[11] + m[1] * m[7]  * m[10] + m[5] * m[2] * m[11] - m[5] * m[3] * m[10] - m[9]  * m[2] * m[7]  + m[9]  * m[3] * m[6]
    inv[7]  =  m[0] * m[6]  * m[11] - m[0] * m[7]  * m[10] - m[4] * m[2] * m[11] + m[4] * m[3] * m[10] + m[8]  * m[2] * m[7]  - m[8]  * m[3] * m[6]
    inv[11] = -m[0] * m[5]  * m[11] + m[0] * m[7]  * m[9]  + m[4] * m[1] * m[11] - m[4] * m[3] * m[9]  - m[8]  * m[1] * m[7]  + m[8]  * m[3] * m[5]
    inv[15] =  m[0] * m[5]  * m[10] - m[0] * m[6]  * m[9]  - m[4] * m[1] * m[10] + m[4] * m[2] * m[9]  + m[8]  * m[1] * m[6]  - m[8]  * m[2] * m[5]

    det = m[0] * inv[0] + m[1] * inv[4] + m[2] * inv[8] + m[3] * inv[12]
    for i in range(16):
        inv[i] /= det
    return inv

def get_camera_position():
    viewMatrix = glGetFloatv(GL_MODELVIEW_MATRIX)
    invVM      = InverseMat44(viewMatrix)
    return (invVM[12], invVM[13], invVM[14])



def create_targets():
    targets = []
    for _ in range(30):
        targets.append(cube(texture1))

    cordZ = -7
    cordX = -9
    for i in range(0,10):
        targets[i].add_to_x(cordX)
        targets[i].add_to_y(0)
        targets[i].add_to_z(cordZ)
        cordX += 2


    cordX = -9
    for i in range(10,20):
        targets[i].add_to_x(cordX)
        targets[i].add_to_y(2)
        targets[i].add_to_z(cordZ)
        cordX += 2

    cordX = -9
    for i in range(20,30):
        targets[i].add_to_x(cordX)
        targets[i].add_to_y(4)
        targets[i].add_to_z(cordZ)
        cordX += 2

    return targets



# static options
clip_away = 30
cube_speed = 0.5
texture1 = "5/textures/t3.jpg"
texture2 = "5/textures/t2.jpg"



# pygame setup
pygame.init()
display = (1000,900)
pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

displayCenter = [display[i] // 2 for i in range(2)]
pygame.mouse.set_pos(displayCenter)

# camera setup
gluPerspective(45, (display[0]/display[1]), 0.1, clip_away)
glTranslatef(0.0, 0.0, 0)

glEnable(GL_TEXTURE_2D)
glEnable(GL_DEPTH_TEST)


# generate targets
targets = create_targets()
thrown_cubes = []


# frame loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        # move screen on mouse move
        if event.type == pygame.MOUSEMOTION:
            relative_movement = pygame.mouse.get_rel() # The relative movement of the mouse
            glRotatef(relative_movement[1]*0.1, 1,0,0)
            glRotatef(relative_movement[0]*0.3, 0,1,0)


        # throw cube on space key press
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                cam_x, cam_y, cam_z = get_camera_position()
                # print(cam_x, cam_y, cam_z)

                # create the cube and resize it
                c = cube(texture2)
                c.change_size(.10)
                c.set_acceleration_cords(cam_x, cam_y, cam_z)
                thrown_cubes.append(c)


    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)


    # draw remaining targets
    if(targets):
        for t in targets:
            t.draw()

    # draw if there is any cube on the air
    if(thrown_cubes):
        # move cubes
        for c in thrown_cubes:
            c.draw()
            c.accelerate_cube(cube_speed)

            # delete targets on collision
            targets = [t for t in targets if not t.check_Collision(c)]

        # delete thrown cubes if they are far away
        thrown_cubes = [c for c in thrown_cubes if not c.get_largest_abs_cord() > clip_away]

    

    pygame.display.flip()
    pygame.time.wait(10)


