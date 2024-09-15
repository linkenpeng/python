#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 15:26:54 2024

@author: pengzhenxian
"""

class TrieTree(object):
    def __init__(self):
        self.size = 0
        self.chidren = [None] * 26

    def insert(self, word):
        node = self
        for w in word:
            index = ord(w) - 97
            node.size += 1
            if node.chidren[index] == None:
                node.chidren[index] = TrieTree()
            node = node.chidren[index]
    
    def search(self, word):
        node = self
        for w in word:
            index = ord(w) - 97
            if node.chidren[index] == None:
                return 0
            else:
                node = node.chidren[index]
        return node.size
        
def main():
    tree = TrieTree()
    tree.insert('aabb')
    tree.insert('abcd')
    tree.insert('efgd')
    tree.insert('adwq')
    tree.insert('gthy')
    tree.insert('asked')
    
    print(tree.search('a'))
    print(tree.search('ef'))
    
    
if __name__ == '__main__': 
    main()
            