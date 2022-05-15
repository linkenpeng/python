# coding=gb2312
#/usr/bin/env python (1)��ʼ��

import os

def printOs():
    print(os.sep)
    print(os.linesep)
    print(os.pathsep)
    print(os.curdir)
    print(os.pardir)
    print(__file__)
    print(os.path.dirname(__file__))
    os.system("ls -a")


def pathTest(path):
    print(os.path.abspath(path))
    print(os.path.normpath(path))
    print(os.path.realpath(path))
    print(os.path.dirname(path))
    print(os.path.basename(path))
    print(os.path.join(path))
    print(os.path.exists(path))
    print(os.path.isfile(path))
    print(os.path.isdir(path))
    print(os.path.getatime(path))
    print(os.path.getmtime(path))
    print(os.path.getctime(path))
    print(os.path.getsize(path))


def cleanTemp():
    for tmpdir in ('/tmp','C:\TEMP'):
        if os.path.isdir(tmpdir):
            break
        else:
            print('no temp directory available')
            tmpdir = ''

    if tmpdir:
        os.chdir(tmpdir)
        cwd = os.getcwd()
        print('*** current temporary directory')
        print(cwd)

        print('*** creating example directory...')
        os.mkdir('example')
        os.chdir('example')
        cwd = os.getcwd()
        print('*** new working directory')
        print(cwd)
        print('*** original directory listing:')
        print(os.listdir(cwd))

        print('*** creating test file....')
        fobj = open('test', 'w')
        fobj.write('foo\n')
        fobj.write('bar\n')
        fobj.close()
        print('*** updated directory listing:')
        print(os.listdir(cwd))

        print('*** renaming "test" to "filetest.txt"')
        os.rename('test', 'filetest.txt')
        print('*** updated directory listing: ')
        print(os.listdir(cwd))

        path = os.path.join(cwd, os.listdir(cwd)[0])
        print('*** full file pathname')
        print(path)
        print('*** (pathname, basename) ==')
        print(os.path.split(path))
        print('*** (filename, extention) ==')
        print(os.path.splitext(os.path.basename(path)))

        print('*** displaying file contents: ')
        fobj = open(path)
        for eachLine in fobj:
            print(eachLine)
        fobj.close()

        print('*** deleting test file')
        os.remove(path)
        print('*** updated directory listing: ')
        print(os.listdir(cwd))
        os.chdir(os.pardir)
        print('*** deleting test directory')
        os.rmdir('example')
        print('*** DONE')

printOs()