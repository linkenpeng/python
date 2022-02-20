#/usr/bin/env/ python
# -*- coding: utf-8 -*-
'''
opencv 测试
'''

import cv2

'''
自动生成素描草图
'''
def autoImage():
    img = cv2.imread("/Users/pengzhenxian/Downloads/照片/形象1.jpg")

    ## Image to Gray Image
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ## Gray Image to Inverted Gray Image
    inverted_gray_image = 255 - gray_image

    ## Blurring The Inverted Gray Image
    blurred_inverted_gray_image = cv2.GaussianBlur(inverted_gray_image, (19,19),0)

    ## Inverting the blurred image
    inverted_blurred_image = 255 - blurred_inverted_gray_image

    ### Preparing Photo sketching
    sketck = cv2.divide(gray_image, inverted_blurred_image, scale= 256.0)

    cv2.imshow("Original Image", img)
    cv2.imshow("Pencil Sketch", sketck)
    cv2.waitKey(0)

if __name__ == '__main__':
    autoImage()