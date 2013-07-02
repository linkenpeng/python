#/usr/bin/env python
# coding:utf-8  
import re, urllib2, os, datetime, urlparse 
HOST_NAME = 'huaban.com'
VISIT_SITE = "http://www." + HOST_NAME 
HAS_MEET_PAGES = [VISIT_SITE] 
LEFT_PAGES = [VISIT_SITE] 
MAIN_CNT = 1 
PATTERN = re.compile('(href|src|area)="([^\s;]+)"') 
EXTS = ['jpg','jpeg','png','gif','bmp']

def main(LEFT_PAGES): 
    if len(LEFT_PAGES) == 0: 
        print("没有需要访问的网页了，END")
        return 
    else: 
        global MAIN_CNT 
        print("...第%s次递归进入MAIN函数..." % MAIN_CNT)
        tmp_pages = [] 
        for page in LEFT_PAGES: 
            tmp_pages.append(page) 
        
        print(tmp_pages)
        
        for url in tmp_pages: 
            print("准备获取网页:%s" % url)
            try: 
                resp = urllib2.urlopen(url) 
            except urllib2.HTTPError as err: 
                print(err.code, url)
                continue 
            finally: 
                LEFT_PAGES.remove(url) 
             
            source = resp.read() 
            current_url = resp.geturl() 
            content_type = resp.headers.get("Content-Type") 
            resp.close() 
            
            # 保存文件  
            if source is not None: 
                ext = getExt(url)
                if ext in EXTS:
                    src_dir = os.path.dirname(__file__) 
                    filename = os.path.join(src_dir, "source", datetime.datetime.now().strftime("%Y%m%d.%H%M%S%f") + "." + ext) 
                    makeDirs(filename)
                    fp = file(filename, "wb") 
                    fp.write(source) 
                    fp.close() 
                # 抽取链接  
                hrefs = re.findall(PATTERN, source) 
                if len(hrefs) > 0: 
                    for url in hrefs: 
                        href = url[1] 
                        href = urlparse.urljoin(current_url, href) 
                        href = href.replace("/../", "/") 
                        if href not in HAS_MEET_PAGES: 
                            HAS_MEET_PAGES.append(href) 
                            if urlparse.urlparse(href).hostname is not None and HOST_NAME in urlparse.urlparse(href).hostname: 
                                LEFT_PAGES.append(href)
     
    MAIN_CNT += 1 
    main(LEFT_PAGES) 

def getExt(filename):
    return filename[filename.rindex('.')+1 : len(filename)]

def makeDirs(filename):
        filename = filename.replace('\\', '/')
        if os.path.isdir(filename):
            dir = filename
        else:
            dir = filename[0 : filename.rindex('/')]
        if not os.path.exists(dir):
            os.makedirs(dir, 777)
                 
if __name__ == '__main__':     
    main(LEFT_PAGES)








