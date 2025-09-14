data = input("please input 3 integers:")
l1, l2, l3 = data.split();
print(l1, l2, l3)
print(type(l2))

i_list= map(int, data.split());
for i in i_list:
    print("{} {}".format(type(i), i))
