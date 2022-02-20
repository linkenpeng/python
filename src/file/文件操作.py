raw_input = input
filename = input('Enter file name:')
fobj = open(filename, 'r')
for eachLine in fobj:
    print(eachLine,end=' ')
fobj.close()