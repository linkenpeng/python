#!/usr/bin/env python3# -*- coding: utf-8 -*-"""可以找最短路径可以生成新的边"""import networkx as nximport matplotlib.pyplot as pltdef img1():    G = nx.erdos_renyi_graph(10, 0.2)    draw_img(G)def img2():    G = nx.watts_strogatz_graph(10, 3, 0.4)    draw_img(G)def draw_img(G):    for n1, n2 in G.edges():        print('From node: ', n1, ' to Node:', n2)    nx.draw_networkx(G)    plt.axis('off')    plt.show()    img2()    