# 汉诺塔
count = 1
def hanoi(n, src, dst, mid):
    global count
    if n == 1:
        print("step:{} {}:{}->{}".format(count, 1, src, dst))
        count += 1
    else:
        hanoi(n-1, src, mid, dst)
        print("step:{} {}:{}->{}".format(count, n, src, dst))
        count += 1
        hanoi(n-1, mid, dst, src)

hanoi(8, "A", "C", "B")
print(count)