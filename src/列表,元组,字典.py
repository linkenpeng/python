# coding=gb2312

print("列表")
aList = [1, 2, 3, 4]
print(aList)
print(aList[0])
print(aList[2:])
print(aList[:3])
aList[1] = 5
print(aList)
print('-' * 30)

print('元组')
aTuple = ('robots', 77, 93, 'try')
print(aTuple)
print(aTuple[:3])
# 元组不可修改 aTuple[1] = 5 
# TypeError: 'tuple' object does not support item assignment
print('-' * 30)

print('字典')
aDict = {'host': 'earth'}
aDict['port'] = 80
print(aDict)
print(aDict.keys())
print(aDict['host'])
print('遍历字典')
for key in aDict:
    print(key, aDict[key])









