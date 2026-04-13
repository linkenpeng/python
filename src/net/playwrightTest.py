'''
pip install playwright
playwright install
palywright --version
'''
from playwright.sync_api import sync_playwright
import time

def test_open_baidu():
    # 启动浏览器
    with sync_playwright() as p:
        # 启动 Chrome，visible=True 表示显示浏览器窗口
        browser = p.chromium.launch(headless=False, slow_mo=500)
        
        # 新建页面
        page = browser.new_page()
        
        # 打开网页
        page.goto("https://www.baidu.com")
        
        # 输入搜索内容
        page.fill("#chat-textarea", "你好 Playwright")
        
        # 点击搜索
        page.click("#chat-submit-button")
        
        # 等待 3 秒
        time.sleep(3)
        
        # 关闭浏览器
        browser.close()

def auto_login():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=300)
        page = browser.new_page()

        # 打开登录页
        page.goto("")

        # 输入账号密码
        page.fill("#login", "")
        page.fill("#password", "")

        # 点击登录
        page.click("#submit")

        # 等待登录成功
        page.wait_for_url("**/dashboard**")

        print("登录成功！")
        browser.close()

if __name__ == '__main__': 
    test_open_baidu()