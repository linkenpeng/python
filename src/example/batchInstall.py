import os
libs = [
    "requests", # HTTP协议访问及网络爬虫
    "jieba", # 中文分词
    "mysql",
    "redis",
    "lxml",
    "beautifulsoup4", #HTML和XML解析器
    "pymongo",
    "uiautomator",
    "opencv-python",
    "pyquery",
    "pandas", # 高效数据分析和计算
    "numpy", # N维数据表示和运算
    "matplotlib", # 二维数据可视化
    "pillow", # 图像处理
    "sklearn", # 机器学习和数据挖掘
    "wheel", # Python第三方库文件打包工具
    "pyinstaller", # 打包Python源文件为可执行文件
    "django", # Python最流行的web开发框架
    "flask", # 轻量级web开发框架
    "werobot", # 微信机器人开发框架
    "sympy", # 数学符号计算工具
    "networkx", # 复杂网络和图结构的建模和分析
    "pyqt5", # 基于Qt的专业级GUI开发框架
    "pyopengl", # 多平台OpenGL开发接口
    "pypdf2", # PDF文件内容提取及处理
    "docopt", # Python命令行解析
    "pygame" # 简单小游戏开发框架
]

try:
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
    print("")

except:
    print("Failed Somehow")
