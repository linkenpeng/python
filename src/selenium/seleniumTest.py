#/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

def test():
    # driverJs = webdriver.PhantomJS('./phantomjs')
    driver = webdriver.Chrome('/Users/pengzhenxian/Downloads/software/chromedriver')
    driver.get('https://www.baidu.com')

    '''
    time.sleep(5)
    html = driver.page_source
    print(html)
    '''

    try:
        WebDriverWait(driver,5).until(EC.presence_of_element_located((By.CLASS_NAME, "btn_wr"), '通关'))
    except Exception as _:
        print('网页加载太慢，不想等了')
    print(driver.page_source)

    input('按任意键结束。')

if __name__ == '__main__':
    test()