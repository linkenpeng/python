#/usr/bin/env python
# coding:utf-8  
import re, urllib2, os, datetime, urlparse 
 
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
         
        for each in tmp_pages: 
            print("准备获取网页:%s" % each)
            try: 
                resp = urllib2.urlopen(each) 
            except urllib2.HTTPError as err: 
                print(err.code, each)
                continue 
            finally: 
                LEFT_PAGES.remove(each) 
             
            source = resp.read() 
            current_url = resp.geturl() 
            content_type = resp.headers.get("Content-Type") 
            resp.close() 
            # 保存图片文件  
        if content_type is not None: 
            type1, type2 = content_type.split(";")[0].split("/") 
            if type1 is not None and type2 is not None and type1.lower() == "image": 
                src_dir = os.path.dirname(__file__) 
                filename = os.path.join(src_dir, "source", datetime.datetime.now().strftime("%Y%m%d.%H%M%S%f") + "." + type2) 
                fp = file(filename, "wb") 
                fp.write(source) 
                fp.close() 
            # 抽取链接  
            hrefs = re.findall(PATTERN, source) 
            if len(hrefs) > 0: 
                for each in hrefs: 
                    href = each[1] 
                    href = urlparse.urljoin(current_url, href) 
                    href = href.replace("/../", "/") 
                    if href not in HAS_MEET_PAGES: 
                        HAS_MEET_PAGES.append(href) 
                        if urlparse.urlparse(href).hostname is not None and "renrendai.com" in urlparse.urlparse(href).hostname: 
                            LEFT_PAGES.append(href) 
     
    MAIN_CNT += 1 
    main(LEFT_PAGES) 
 
if __name__ == '__main__': 
    VISIT_SITE = "http://www.renrendai.com/" 
    HAS_MEET_PAGES = [VISIT_SITE] 
    LEFT_PAGES = [VISIT_SITE] 
    MAIN_CNT = 1 
    PATTERN = re.compile('(href|src|area)="([^\s;]+)"') 
    main(LEFT_PAGES)
