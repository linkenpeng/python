# coding=gb2312

print("��Ƭ����,����������������")
s = 'abcdefgh'
print(s[::-1]) #������������ת������
print(s[::2])   #��һ��ȡһ��

print("range(a,b,c) ����a-b����c���б�����b")
for i in range(-1, -len(s), -1):
    print(i,s[:i])
    
hi = '''
hi
there
    '''

print(repr(hi))
print(hi)

print(id(hi))