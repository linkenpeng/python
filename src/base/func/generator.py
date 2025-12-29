def my_generator():
    for i in range(5):
        yield i

gen = my_generator()
for num in gen:
    print(num)