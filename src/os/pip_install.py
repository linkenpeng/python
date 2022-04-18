import os
libs = [
    "requests",
    "jieba",
    "mysql",
    "redis",
    "lxml",
    "beautifulsoup4",
    "pymongo",
    "uiautomator",
    "opencv-python",
    "pyquery",
    "pandas"
]

command = input("请输入i/u/l：")
for lib in libs:
    if command == "i":
        os.system("pip install " + lib)
    elif command == "u":
        os.system("pip uninstall " + lib)
    elif command == "l":
        print("当前安装的类库有：", libs)
        exit()
    else:
        print("输入指令错误, i:install u:uninstall l:list")
        exit()


