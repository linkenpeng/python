# coding=gb2312
#!/usr/bin/env python

def showMaxFactor(num):
    count = num / 2
    while count > 1:
        if num % count == 0:
            print('largest factor of %d is %d' % (num, count))
            break
            count -= 1
        else:
            print(num,'is prime')

for eachNum in range(10, 21):
    print(showMaxFactor(eachNum))
    
    