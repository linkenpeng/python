
a = 123.534
b = -99.989
c = 100

def printMathFunc():
    print(abs(b))
    print(divmod(a, 10))
    print(pow(3,3))
    print(round(a))
    print(max(a,b))
    print(min(a,b))
    print(int(a))
    print(int(b))
    print(float(c))
    print(complex(c))

def equalsTow(a, ap, b, bp, aname, bname, unit):
    print("{2}GDP基数：{0}{3} {2}GDP增速:{1}%".format(a, ap * 100, aname, unit))
    print("{2}GDP基数：{0}{3} {2}GDP增速:{1}%".format(b, bp * 100, bname, unit))
    for i in range (1, 100):
        ta = int(a * pow(1 + ap, i))
        tb = int(b * pow(1 + bp, i))
        print("第{0}年 {3}：{1}{5} {4}：{2}{5} ".format(i, ta, tb, aname, bname, unit))
        if ta >= tb :
            break;

equalsTow(2000, 0.113, 12000, 0.083, "海口", "佛山", "亿元")

equalsTow(17.7, 0.06, 23, 0.03,  "中国", "美国", "万亿美元")