# coding=utf-8
import threading
import time
import random


class AccessUrl(threading.Thread):
    """访问url"""
    def __init__(self, host):
        threading.Thread.__init__(self)
        self.host = host

    def run(self):
        k = random.randint(1, 10)
        print "Processing " + self.host + " waiting for : " + str(k)
        time.sleep(k)
        print "exiting " + self.host
        pool.release()


class Handler(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        for i in hosts:
            pool.acquire()
            t = AccessUrl(i)
            t.setDaemon(True)
            t.start()


# 设置初始信号量数值为2,意味着release()调用次数不能超过初始值
maxconn = 2

# 有限(bounded)信号量
pool = threading.BoundedSemaphore(value=maxconn)

# 临界资源
hosts = ["http://yahoo.com",
         "http://google.com",
         "http://amazon.com",
         "http://ibm.com",
         "http://apple.com"]

handler = Handler()
handler.start()
handler.join()

print "exiting main"