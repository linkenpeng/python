
try:
    filename = input('Enter file name: ')
    fobj = open(filename, 'r')
    for eachLine in fobj:
        print(eachLine,)
    fobj.close()
except IOError as e:
    print('file open error: ', e)