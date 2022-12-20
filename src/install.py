#!/usr/bin/env python

import os

libs = ["requests", "jieba", "mysql", "redis", "lxml", "beautifulsoup4"
    ,"pymongo", "uiautomator", "opencv-python",
        "pyquery", "pandas", "hashlib","pyinstaller",
        "wordcloud", "matplotlib", "imageio"]

for lib in libs:
    os.system("pip install " + lib)