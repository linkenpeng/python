# coding=gb2312

print("�б�")
aList = [1, 2, 3, 4]
print(aList)
print(aList[0])
print(aList[2:])
print(aList[:3])
aList[1] = 5
print(aList)
print('-' * 30)

print('Ԫ��')
aTuple = ('robots', 77, 93, 'try')
print(aTuple)
print(aTuple[:3])
# Ԫ�鲻���޸� aTuple[1] = 5 
# TypeError: 'tuple' object does not support item assignment
print('-' * 30)

print('�ֵ�')
aDict = {'host': 'earth'}
aDict['port'] = 80
print(aDict)
print(aDict.keys())
print(aDict['host'])
print('�����ֵ�')
for key in aDict:
    print(key, aDict[key])









