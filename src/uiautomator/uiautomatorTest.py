#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''

uiautomator 测试

pip install uiautomator
启动 android_sdk/tools/bin/uiautomator

'''

from uiautomator import Device

def test():
    device = Device()
    print(device.dump())
    device(text='微信').click()

if __name__ == '__main__':
    test()