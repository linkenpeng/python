# 删除一个文件夹下面的重复文件
import hashlib
import os  
from time import clock as now  
def getmd5(filename):  
    file_txt = open(filename,"rb").read()  
    md5 = hashlib.md5()
    m = md5.new(file_txt)  
    return m.hexdigest()  
def main():
    path = input("path:")
    all_size = {}  
    total_file = 0 
    total_delete = 0 
    start = now()  
    for file in os.listdir(path):  
        total_file += 1  
        real_path = os.path.join(path, file)  
        if os.path.isfile(real_path) == True:  
            size = os.stat(real_path).st_size  
            name_and_md5 = [real_path, '']  
            if size in all_size.keys():  
                new_md5 = getmd5(real_path)  
                if all_size[size][1] == '':  
                    all_size[size][1] = getmd5(all_size[size][0])  
                if new_md5 in all_size[size]:  
                    print ('删除'), file  
                    total_delete += 1  
                else:  
                    all_size[size].append(new_md5)  
            else:  
                all_size[size] = name_and_md5  
    end = now()  
    time_last = end - start  
    print ('文件总数：'), total_file  
    print ('删除个数：'), total_delete  
    print ('耗时：'), time_last, '秒'  
      
if __name__ == '__main__':   
    main()  
