
# 上下文管理器用于管理资源的分配和释放，确保在代码块执行结束后，相关资源（如文件、数据库连接等）能被正确关闭。
# 应用场景：文件操作、数据库连接管理等场景。
class FileManager():
    def __init__(self, filename, mode):
        print('__init__')
        self.filename = filename
        self.mode = mode
        self.file = None
    
    def __enter__(self):
        print('__enter__')
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, ec_val, exc_tb):
        print('__exit__')
        if self.file:
            self.file.close()

with FileManager('test_data/test1.txt', 'w') as f:
    print('write')
    f.write('this is a test')

