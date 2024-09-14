#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  8 09:17:57 2024

@author: pengzhenxian
"""
import random as rd
from inpututil import InputUtil

class BTree:
    class _Node:
        def __init__(self, data = 0):
            self._data = data
            self._left = None
            self._right = None
            self._parent = None
        
    def __init__(self):
        self._root = None
        
    def insert(self, data):
        if(self._root == None):
            self._root = self._Node(data)
            return
        p = self._root
        while p._data != data:
            if p._data < data:
                if p._right == None:
                    break
                else: 
                    p = p._right
            elif p._left == None:
                break
            else:
                p = p._left
        
        if p._data < data:
            node = self._Node(data)
            p._right = node
        elif p._data > data:
            node = self._Node(data)
            p._left = node
            
        return
            
    # 递归插入
    def insert_rec(self, data, node = None):
        if (self._root == None):
            self._root = self._Node(data)
            return self._root
        if node == None:
            node = self._root
        if node._data == data:
            return node
        elif node._data < data:
            if node._right == None:
                node._right = self._Node(data)
            else:
                node._right = self.insert_rec(data, node._right)
        else:
            if node._left == None:
                node._left = self._Node(data)
            else:
                node._left = self.insert_rec(data, node._left)
        return node
    
    def search(self, data):
        p = self._root
        while p != None:
            if p._data == data:
                return True
            elif p._data < data:
                p = p._right
            else:
                p = p._left
        return False
    
    # 递归查找
    def search_rec(self, data, node = None):
        if node == None:
            p = self._root
        else:
            p = node
            
        if p._data == data:
            return True
        elif p._data < data:
            if (p._right == None):
                return False
            else:
                return self.search_rec(data, p._right)
        else:
            if (p._left == None):
                return False
            else:
                return self.search_rec(data, p._left)
        return False
    
    def printTree(self, node):
        if node != None:
            if (node._left != None):
                self.printTree(node._left)
            print(node._data)
            if (node._right != None):
                self.printTree(node._right)
                
    def printSearchResult(self, data, result):
        if (result):
            print(f'{data} in tree')
        else:
            print(f'{data} not in tree')
    
def main():
    n = rd.randint(1, 20)
    print(n)
    tree = BTree()
    for i in range(n):
        d = rd.randint(1, 100)
        print(d)
        tree.insert_rec(d)
        
    print('-' * 30)
    tree.printTree(tree._root)
    
    data = InputUtil.inputOne(int, '请输出需要查找的数:')
    search_result = tree.search(data)
    tree.printSearchResult(data, search_result)

if __name__ == '__main__': 
    main()
    
    
    
    
    








        
            
            
            