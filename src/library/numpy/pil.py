#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 18:42:55 2023

@author: pengzhenxian
"""
from PIL import Image
import numpy as np

def pilImage(image_file):
    image_files = image_file.split('.')
    im = np.array(Image.open(image_file))
    print(im.shape, im.dtype)
    
    # 补码变换
    b = [255, 255, 255] - im
    print(b)
    c = Image.fromarray(b.astype('uint8'))
    c.save(image_files[0] + "_2." + image_files[0])
    
    # 灰度变换
    d = np.array(Image.open(image_file).convert('L'))
    e = 255 - d
    f = Image.fromarray(e.astype('uint8'))
    f.save(image_files[0] + "_3." + image_files[0])
    
    # 区间变换
    e = (100/255)*d + 150
    f = Image.fromarray(e.astype('uint8'))
    f.save(image_files[0] + "_4." + image_files[0])
    
    # 区间变换
    e = 255 * (d/255)**2
    f = Image.fromarray(e.astype('uint8'))
    f.save(image_files[0] + "_5." + image_files[0])

# 手绘画图效果
def manualImage(image_file):
    a = np.array(Image.open(image_file).convert('L')).astype('float')
    
    depth = 10. 						    # (0-100)
    grad = np.gradient(a)				#取图像灰度的梯度值
    grad_x, grad_y = grad 				#分别取横纵图像梯度值
    grad_x = grad_x*depth/100.
    grad_y = grad_y*depth/100.
    A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
    uni_x = grad_x/A
    uni_y = grad_y/A
    uni_z = 1./A
    
    vec_el = np.pi/2.2 					# 光源的俯视角度，弧度值
    vec_az = np.pi/4. 					# 光源的方位角度，弧度值
    dx = np.cos(vec_el)*np.cos(vec_az) 	#光源对x 轴的影响
    dy = np.cos(vec_el)*np.sin(vec_az) 	#光源对y 轴的影响
    dz = np.sin(vec_el) 				#光源对z 轴的影响
    
    b = 255*(dx*uni_x + dy*uni_y + dz*uni_z) 	#光源归一化
    b = b.clip(0,255)
    
    im = Image.fromarray(b.astype('uint8')) 	#重构图像
    save_images = image_file.split('.')
    im.save(save_images[0] + '_1.' +  save_images[1])
    

manualImage("/Users/pengzhenxian/Pictures/douyin/5.jpeg")