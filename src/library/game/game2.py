'''
PyGame(http://www.pygame.org): 简单的游戏开发功能库
pip install pygame
python -m pygame.examples.aliens

Panda3D(http://www.panda3d.org): 开源、跨平台的3D渲染和游戏开发库，一个3D游戏引擎，提供Python和C++两种接口
cocos2d（http://python.cocos2d.org): 构建2D游戏和图形界面交互式应用的框架， 提供基于OpenGL的游戏开发图形渲染功能，支持GPU加速
'''

import pygame
from pygame.locals import *
from sys import exit
import random

screen_width = 800
screen_height = 600

pygame.init()
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('this is my first game')

path = './resources/imgs/'

class Animal():
    def __init__(self, name, img_path, width, height):
        self._name = name
        self._img_path = img_path
        self._width = width
        self._height = height
    
    def get_img(self):
        img = pygame.image.load(self._img_path)
        # scale: 设置缩放 flip:翻转 rotate:旋转
        img = pygame.transform.scale(img, [self._width, self._height])
        return img
    
    def get_pos(self):
        posx = random.randint(0, screen_width - self._width)
        posy = random.randint(0, screen_height - self._height)
        return [posx, posy]
        

def get_back_img():
    sea_name = path + 'sea.jpg'
    back_img = pygame.image.load(sea_name)
    return back_img
    
Fish = Animal('fish', path + 'fish.png', 100, 70)
fish_speed = random.randint(50, 200)
fish_pos = Fish.get_pos()

Sheep = Animal('sheep', path + 'sheep.png', 150, 150)
sheep_pos = Sheep.get_pos()

clock = pygame.time.Clock()
clock.tick(30)  # limits FPS to 30
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            running = False
            exit

    #screen.fill((0, 0, 0))
    time_eplased = clock.tick() / 1000
    fish_pos[0] += fish_speed * time_eplased
    fish_pos[1] += fish_speed * time_eplased
    
    screen.blit(get_back_img(), [0,0])
    screen.blit(Fish.get_img(), fish_pos)
    screen.blit(Sheep.get_img(), sheep_pos)
    
    pygame.display.update()
    

pygame.quit()

    
    
    
    
    
    
    
    
    
    
    
    
