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
    def __init__(self, img, width, height, posx, posy, speedx, speedy, anl = 0):
        self.img = img
        self.width = width
        self.height = height
        self.posx = posx
        self.posy = posy
        self.speedx = speedx
        self.speedy = speedy
        self.fish = pygame.transform.scale(self.img, [self.width, self.height])
        if anl != 0:
            self.fish = pygame.transform.rotate(self.fish, anl)
        
    def update(self, time_eplased):
        self.posx += time_eplased * self.speedx
        self.posy += time_eplased * self.speedy
        
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
            self.speedx = speed
            self.speedy = speed
        else:
            self.speedx *= -1
            self.speedy *= -1
    
    def getImg(self):
        return self.img
    
    def print(self):
        print(self.width, self.height, self.posx, self.posy, self.speed)
    
    def draw(self):
        screen.blit(self.fish, [self.posx, self.posy])
    
    def setDirect(self, angle):
        self.fish = pygame.transform.rotate(self.fish, angle)
    
    def getRect(self):
        rect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        return rect
        
    def collide(self, rect):
        myrect = pygame.Rect(self.posx, self.posy, self.width, self.height)
        return pygame.Rect.colliderect(myrect, rect)
    
    def get_score(self):
        return random.randint(1, 10)

def get_fish_img():
    fish_img_src = path + 'fish.png'
    fish_img = pygame.image.load(fish_img_src)
    return fish_img

def get_fish_group():
    fish_size_min = 50
    fish_size_max = 300
    fish_num = 10
    fish_group = list()
    fish_img = get_fish_img()
    for i in range(fish_num):
        fish_width = random.randint(fish_size_min, fish_size_max)
        fish_height = random.randint(fish_size_min, fish_size_max)
        fish_posx = random.randint(0, screen_width - fish_width)
        fish_posy = random.randint(screen_height/2, screen_height - fish_height)
        fish_speed = random.randint(50, 200)
        fish = Fish(fish_img, fish_width, fish_height, fish_posx, fish_posy, fish_speed, 0, 0)
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

def add_fish(fish_group):
    fish_width = random.randint(50, 100)
    fish_height = random.randint(50, 100)
    direct = random.randint(0, 3)
    if direct == 0:
        fish_posx = 0
        fish_posy = random.randint(0, screen_height - fish_height)
        fish_speedx = random.randint(50, 200)
        fish_speedy = 0
        anl = 0
    elif direct == 1:
        fish_posx = screen_width - fish_width
        fish_posy = random.randint(0, screen_height - fish_height)
        fish_speedx = -random.randint(50, 200)
        fish_speedy = 0
        anl = 180
    elif direct == 2:
        fish_posx = random.randint(0, screen_width - fish_width)
        fish_posy = 0
        fish_speedx = 0
        fish_speedy = random.randint(50, 200)
        anl = 270
    elif direct == 3:
        fish_posx = random.randint(0, screen_width - fish_width)
        fish_posy = screen_height - fish_height
        fish_speedx = 0
        fish_speedy = -random.randint(50, 200)
        anl = 90    
    fish = Fish(get_fish_img(), fish_width, fish_height, fish_posx, fish_posy, fish_speedx, fish_speedy, anl)
    fish_group.append(fish)
    
    
#fish_group = get_fish_group()
fish_group = list()

Sheep = Animal('sheep', path + 'sheep.png', 150, 150)
sheep_pos = Sheep.get_pos()
sheep_size = Sheep.get_size()
sheep_speed = 100

clock = pygame.time.Clock()
clock.tick(30)  # limits FPS to 30
running = True
in_screen = True
kill = False
mouse_used = True
score = 0
font = pygame.font.SysFont('arial', 24)
pygame.time.set_timer(USEREVENT + 1, 2000)
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            running = False
            exit
        elif event.type == USEREVENT + 1:
            add_fish(fish_group)
        if mouse_used:
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = pygame.mouse.get_pos()
                sheep_pos[0] = x - sheep_size[0] / 2
                sheep_pos[1] = y - sheep_size[1] / 2
            
    #screen.fill((0, 0, 0))
    time_eplased = clock.tick() / 1000
    
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
        sheep_pos[0] -= sheep_speed * time_eplased
        if sheep_pos[0] <= 0:
            sheep_pos[0] = 0
    elif key[pygame.K_RIGHT]:
        sheep_pos[0] += sheep_speed * time_eplased
        if sheep_pos[0] > screen_width - sheep_size[0]:
            sheep_pos[0] = screen_width - sheep_size[0]
    if key[pygame.K_UP]:
        sheep_pos[1] -= sheep_speed * time_eplased
        if sheep_pos[1] <= 0:
            sheep_pos[1] = 0
    elif key[pygame.K_DOWN]:
        sheep_pos[1] += sheep_speed * time_eplased
        if sheep_pos[1] > screen_height - sheep_size[1]:
            sheep_pos[1] = screen_height - sheep_size[1]
    
    screen.blit(get_back_img(), [0,0])
    screen.blit(Sheep.get_img(), sheep_pos)
    sheep_rect = pygame.Rect(sheep_pos[0], sheep_pos[1], sheep_size[0], sheep_size[1])
    font_img = font.render('{}.scores'.format(score), False, (0, 0, 0))
    fish_num = len(fish_group)
    for fish in fish_group:
        fish.update(time_eplased)
        in_windows = fish.inWindows(screen_width, screen_height)
        if in_windows == False:
            if kill == True:
                fish_group.remove(fish)
            else:
                fish.setSpeed()
                fish.setDirect(180)
        else:
            collide = fish.collide(sheep_rect)
            if collide:
                score += fish.get_score()
                fish_group.remove(fish)
            else:
                fish.draw()
    font_img = font.render('{}.scores'.format(score), False, (0, 0, 0))
    screen.blit(font_img, [10, 10])
    
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

    
    
    
    
    
    
    
    
    
    
    
    
