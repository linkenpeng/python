import csv
import urllib3
import os

def test():
    with open('test.csv', 'r') as f:
        text = f.read()
    print(text)

    f2 = open('test.csv', 'r')
    text2 = f2.read()
    print(text2)
    f2.close()

    with open('test.csv','w') as f:
        f.write('d,e,f \n')

    with open('test.csv','a') as f:
        f.writelines('j,k,l')

def test_csv():
    with open('test.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)

def test_urllib3():
    print(os.getcwd())
    response = urllib3.Request('http://picm.photophoto.cn/015/037/003/0370030333.jpg');
    rs = urllib3.urlopen(response)
    f = open("pic.jpg",'wb')
    f.write(rs.read())
    f.close()

if __name__ == '__main__':
    test_csv()