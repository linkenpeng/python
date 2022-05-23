### python学习项目
> 该项目主要用来学习python用，时隔7年，重启该项目

7年之前是基于python2的项目，现在python2即将停止更新，且python3的模块已经完善, 因此所有的功能都以python3为基础

python -m pip install --upgrade pip

Requirements

### Some Useful site:
- https://www.python.org/
- https://pypi.org/
- https://python123.io/
- [Python Package Index](https://pypi.org)
- [Anaconda](https://www.continuum.io)
- http://www.lfd.uci.edu/~gohlke/pythonlibs/

```python
import os
libs = ["requests", "jieba", "mysql", "redis", "lxml", "beautifulsoup4"
,"pymongo", "uiautomator", "opencv-python", 
"pyquery", "pandas", "hashlib","pyinstaller", "wordcloud", "matplotlib"]
for lib in libs:
    os.system("pip install " + lib)
```

### PyInstaller 
1. -h 帮助
2. --clean 清理打包过程中的临时文件
3. -D, --onedir 默认值，生成dist文件夹
4. -F, --onefile 在dist文件夹中生成独立的打包文件
5. -i <图标文件名.ico> 指定打包程序使用的图标(icon)文件



