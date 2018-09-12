import time
print(time.time())
print(time.localtime())
print(time.localtime(time.time()))
print(time.asctime())
mytime=(2016,7,27,15,45,23,0,0,0)
print(time.localtime(time.mktime(mytime)))
