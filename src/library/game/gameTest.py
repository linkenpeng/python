'''
PyGame(http://www.pygame.org): 简单的游戏开发功能库
pip install pygame
python -m pygame.examples.aliens

Panda3D(http://www.panda3d.org): 开源、跨平台的3D渲染和游戏开发库，一个3D游戏引擎，提供Python和C++两种接口
cocos2d（http://python.cocos2d.org): 构建2D游戏和图形界面交互式应用的框架， 提供基于OpenGL的游戏开发图形渲染功能，支持GPU加速
'''
import pygame, sys

def py_game_init():
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Pygame游戏之旅")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
        pygame.display.update()

def py_ball_game():
    pygame.init()

    vInfo = pygame.display.Info()
    size = width, heigh = vInfo.current_w, vInfo.current_h

    size = width, height = 600, 400
    speed = [1, 1]
    BLACK = 0, 0, 0
    screen = pygame.display.set_mode(size, pygame.RESIZABLE)
    #screen = pygame.display.set_mode(size, pygame.NOFRAME)
    #screen = pygame.display.set_mode(size, pygame.FULLSCREEN)
    pygame.display.set_caption("Pygame壁球")
    ball = pygame.image.load("PYG02-ball.gif")
    ballrect = ball.get_rect()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        speed[0] = speed[0] if speed[0] == 0 else (abs(speed[0] - 1)*int(speed[0]/abs(speed[0])))
                    elif event.key == pygame.K_RIGHT:
                        speed[0] = speed[0] + 1 if speed[0] > 0 else speed[0] - 1
                    elif event.key == pygame.K_UP:
                        speed[1] = speed[1] + 1 if speed[1] > 0 else speed[1] - 1
                    elif event.key == pygame.K_DOWN:
                        speed[1] = speed[1] if speed[1] == 0 else (abs(speed[1] - 1)*int(speed[1]/abs(speed[1])))
                    elif event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.VIDEORESIZE:
                    size = width, height = event.size[0], event.size[1]
                    screen = pygame.display.set_mode(size, pygame.RESIZABLE)

        ballrect = ballrect.move(speed[0], speed[1])
        if ballrect.left < 0 or ballrect.right > width:
            speed[0] = - speed[0]
        if ballrect.top < 0 or ballrect.bottom > height:
            speed[1] = - speed[1]

        screen.fill(BLACK)
        screen.blit(ball, ballrect)

        pygame.display.update()

py_ball_game()