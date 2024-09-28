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
    
    def get_size(self):
        return self._width, self._height

class Fish():
    def __init__(self, img, width, height, posx, posy, speed):
        self.img = img
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.speed = speed
        self.fish = pygame.transform.scale(self.img, [self.width, self.height])
        
    def update(self, time_eplased):
        self.posx += time_eplased * self.speed
        self.posy += time_eplased * self.speed
        
    def newPos(self, posx, posy):    
        self.posx = posx
        self.posy = posy
    
    def inWindows(self, win_width, win_height):
        out_x = self.posx + self.width < 0 or self.width > win_width
        out_y = self.posy + self.height < 0 or self.height > win_height
        if out_x or out_y:
            return False
        return True
    
    def touchEdge(self, win_width, win_height):
        touch_x = self.posx < 0 or self.posx > win_width - self.width
        touch_y = self.posy < 0 or self.posy > win_height - self.height
        if touch_x or touch_y:
            return True
        return False
    
    def setSpeed(self, speed = None):
        if speed:
            self.speed = speed
        else:
            self.speed *= -1
    
    def getImg(self):
        return self.img
    
    def print(self):
        print(self.width, self.height, self.posx, self.posy, self.speed)
    
    def draw(self):
        screen.blit(self.fish, [self.posx, self.posy])
    

def get_fish_group():
    fish_size_min = 50
    fish_size_max = 300
    fish_num = 10
    fish_group = list()
    fish_img_src = path + 'fish.png'
    fish_img = pygame.image.load(fish_img_src)
    for i in range(fish_num):
        fish_width = random.randint(fish_size_min, fish_size_max)
        fish_height = random.randint(fish_size_min, fish_size_max)
        fish_posx = random.randint(0, screen_width - fish_width)
        fish_posy = random.randint(screen_height/2, screen_height - fish_height)
        fish_speed = random.randint(50, 200)
        fish = Fish(fish_img, fish_width, fish_height, fish_posx, fish_posy, fish_speed)
        fish.print()
        fish_group.append(fish)
        
    return fish_group

def get_back_img():
    sea_name = path + 'sea.jpg'
    back_img = pygame.image.load(sea_name)
    return back_img

def get_fish_by_animal():    
    fish = Animal('fish', path + 'fish.png', 100, 70)
    fish_speed = random.randint(50, 200)
    fish_pos = fish.get_pos()
    fish_size = fish.get_size()
    return fish

fish_group = get_fish_group()

Sheep = Animal('sheep', path + 'sheep.png', 150, 150)
sheep_pos = Sheep.get_pos()

clock = pygame.time.Clock()
clock.tick(30)  # limits FPS to 30
running = True
in_screen = True
kill = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            running = False
            exit

    #screen.fill((0, 0, 0))
    time_eplased = clock.tick() / 1000
    screen.blit(get_back_img(), [0,0])
    screen.blit(Sheep.get_img(), sheep_pos)
    
    fish_num = len(fish_group)
    for fish in fish_group:
        fish.update(time_eplased)
        in_windows = fish.inWindows(screen_width, screen_height)
        if in_windows == False:
            if kill == True:
                fish_group.remove(fish)
            else:
                fish.setSpeed()
        else:
            fish.draw()
    
    '''
    fish_pos[0] += fish_speed * time_eplased
    fish_pos[1] += fish_speed * time_eplased
    
    # touch
    touch_x = fish_pos[0] < 0 or fish_pos[0] > screen_width - fish_size[0]
    touch_y = fish_pos[1] < 0 or fish_pos[1] > screen_height - fish_size[1]
    if touch_x or touch_y:
        fish_speed = - fish_speed
    
    out_x = fish_pos[0] + fish_size[0] < 0 or fish_pos[0] > screen_width
    out_y = fish_pos[1] + fish_size[1] < 0 or fish_pos[1] > screen_height
    if out_x or out_y:
        in_screen = False
    
    if in_screen:
        screen.blit(Fish.get_img(), fish_pos)
    '''
    
    pygame.display.update()
    

pygame.quit()

    
    
    
    
    
    
    
    
    
    
    
    
