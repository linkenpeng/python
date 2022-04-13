import os
libs = ["requests", "jieba", "mysql", "redis", "lxml", "beautifulsoup4"
    ,"pymongo", "uiautomator", "opencv-python", "pyquery", "pandas"]
for lib in libs:
    os.system("pip install " + lib)