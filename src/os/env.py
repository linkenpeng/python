def show_env():
    from pathlib import Path
    import sys, os
    print('脚本文件 :', Path(__file__).resolve())
    print('工作目录 :', os.getcwd())
    print('Python   :', sys.executable)
    print('脚本目录 :', Path(__file__).parent.resolve())

if __name__ == '__main__':
    show_env()