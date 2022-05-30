#/usr/bin/env/ python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

def test():
    # driverJs = webdriver.PhantomJS('./phantomjs')
    driver = webdriver.Chrome('/Users/pengzhenxian/Downloads/software/chromedriver')
    driver.get('https://www.huashengju.com')

    comment = driver.find_element_by_xpath('//div[@id="indexArea"]')
    print(comment.text)

    '''
    time.sleep(5)
    html = driver.page_source
    print(html)
    '''

    try:
        # By.ID, By.CLASS_NAME, By.NAME
        WebDriverWait(driver,30).until(EC.presence_of_element_located((By.XPATH, '//div[@id="Subject"]'), '通关'))
    except Exception as _:
        print('网页加载太慢，不想等了')
    # print(driver.page_source)

    input('按任意键结束。')

def test_login():
    driver = webdriver.Chrome('/Users/pengzhenxian/Downloads/software/chromedriver')
    driver.get('https://www.huashengju.com/user-login.html')

    elem = driver.find_element_by_id("username")
    elem.clear()
    elem.send_keys("username")

    password = driver.find_element_by_id("password")
    password.clear()
    password.send_keys("password")

    input('等待网页点击验证码，回到这里按任意键继续')

    elem.send_keys(Keys.RETURN)

    time.sleep(3)

    print(driver.page_source)

    driver.quit()

if __name__ == '__main__':
    test_login()