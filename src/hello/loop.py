# 循环

def for_test():
    for i in range (1, 6):
        print(i)

    for s in "python":
        if s == "t":
            continue
        print(s, end=",")

    list = [123, "a", "b", True]

    # break 跳出当次最内层循环
    for item in list:
        if item == "b":
            break
        print(item)

def while_test():
    s = "python"
    while s != "":
        for ss in s:
            print(ss)
        s = s[:-1]

def try_test():
    try:
        a, b = map(int, input("请输入2个0-100之间的整数:").split())
    except ValueError:
        a = -1
        b = -1
        print('输入类型错误，请输入2个0-100之间的整数')
    while((a < 0 or a > 100) or (b < 0 or b > 100)):
        try:
            a, b = map(int, input("请输入2个0-100之间的整数:").split())
        except ValueError:
            print('输入类型错误，请输入2个0-100之间的整数')
    s = a + b
    print("{}+{}={}".format(a, b, s))

try_test()