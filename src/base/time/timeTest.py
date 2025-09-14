
import time

gmt = time.gmtime()
print(time.time())
print(time.ctime())
print(gmt)

gmt_str = time.strftime("%Y-%m-%d %H:%M:%S", gmt)
print(gmt_str)
print(time.strptime(gmt_str, "%Y-%m-%d %H:%M:%S"))

start = time.perf_counter()

end = time.perf_counter()

print(end - start)