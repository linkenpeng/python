### python学习项目
> 该项目主要用来学习python用，时隔7年，重启该项目

7年之前是基于python2的项目，现在python2即将停止更新，且python3的模块已经完善, 因此所有的功能都以python3为基础

python -m pip install --upgrade pip

Requirements

### Some Useful site:
- https://www.python.org/
- https://pypi.org/
- https://python123.io/

```python
import os
libs = ["requests", "jieba", "mysql", "redis", "lxml", "beautifulsoup4"
,"pymongo", "uiautomator", "opencv-python", "pyquery", "pandas", "hashlib"]
for lib in libs:
    os.system("pip install " + lib)
```