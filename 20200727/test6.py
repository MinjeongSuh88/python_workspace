import time

print(time.ctime())
print(time.gmtime(),type(time.gmtime()))
print(time.gmtime().tm_mon,type(time.gmtime()))
print(time.gmtime().tm_mday,type(time.gmtime()))

help(time)