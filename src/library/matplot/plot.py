#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 21:40:03 2023

| 函数 | 说明 |
| ------- | --- |
| plt.plot | 坐标图 |
| plt.boxplot | 箱型图 |
| plt.bar | 条形图 |
| plt.barh | 横向条形图 |
| plt.polar | 极坐标图 |
| plt.pie | 饼图 |
| plt.psd | 功率谱密度图 |
| plt.specgram | 谱图 |
| plt.cohere | X-Y的相关性函数 |
| plt.scatter | 散点图，其中，x和y长度相同 |
| plt.step | 步阶图 |
| plt.hist | 直方图 |
| plt.contour | 等值图 |
| plt.vlines | 垂直图 |
| plt.stem | 柴火图 |
| plt.plot_date | 数据日期 |

@author: pengzhenxian
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import matplotlib.gridspec as gridspec


def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def draw():
    a = np.arange(0.0, 5.0, 0.02)
    plt.subplot(211)
    plt.plot(a, f(a))
    plt.subplot(2,1,2)
    plt.plot(a, np.cos(2*np.pi*t), 'r--')
    plt.show()
    
    
def d1():
    plt.plot([0,2,4,6,8], [3, 1, 4, 5, 2])
    plt.ylabel("grade")
    # 行,列,选择区域
    plt.subplot(3,2,4)
    # 前两个x轴 ， 后两个y轴
    plt.axis([-1,10,0,6])
    # plt.savefig("test", dpi=600)
    plt.show()
  
def multi():
    a = np.arange(10)
    plt.plot(a,a*1.5,'go-', a,a*2.5,'rx', a,a*3.5,'*', a,a*4.5,'b-.')
    plt.show()
  
def chinese():
    """
    | 中文字体 | 说明 |
    | ------- | --- |
    | 'SimHei' | 黑体 |
    | 'Kaiti' | 楷体 |
    | 'LiSu' | 隶书 |
    | 'FangSong' | 仿宋 |
    | 'YouYuan' | 幼圆 |
    | 'STSong' | 华文仿宋 |
    """
    # matplotlib.rcParams['font.family'] = 'SimHei'
    # matplotlib.rcParams['font.size'] = 20
    a = np.arange(0.0, 5.0, 0.02)
    plt.xlabel("横轴：时间", fontproperties='SimHei', fontsize=20)
    plt.ylabel("纵轴：振幅", fontproperties='SimHei', fontsize=20)
    # $$ Latex语法
    plt.title("正弦波 $y=cos(2\pi x)$", fontproperties='SimHei', fontsize=25)
    #plt.text(2, 1, r'$\mu=100$', fontsize=15)
    plt.annotate(r'$\mu=100$', xy=(2,1), xytext=(3, 1.5), arrowprops=dict(facecolor='black', shrink=0.1, width=2))
    plt.axis([-1, 6, -2, 2])
    plt.grid(True)
    
    
    plt.plot(a, np.cos(2*np.pi*a), 'r--')
    
    # plt.plot([3, 1, 4, 5, 2])
    # plt.ylabel("数轴（值）")
    # plt.savefig("test", dpi=600)
    plt.show()

"""
def subplotTest():
    gs = gridspec.GridSpec(3, 3)
    ax1 = plt.subplot(gs[0, :])
    ax2 = plt.subplot(gs[1, :-1])
    ax3 = plt.subplot(gs[1:, -1])
    ax4 = plt.subplot(gs[2, 0])
    ax5 = plt.subplot(gs[2, 1])
"""

def pieTest():
    labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
    sizes = [15, 30, 45, 10]
    explode = (0, 0.1, 0, 0)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%',
            shadow=False, startangle=90)
    plt.show()


pieTest()














