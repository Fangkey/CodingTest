# coding=utf-8
from time import sleep
import threading

class Mythread(threading.Thread):
    def __init__(self,func,args):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args

    def run(self):
        apply(self.func,self.args)


def foo(i):
    print '%s starting..' %i
    sleep(i)


threads = []
for i in range(5):
    t = Mythread(foo,(i,))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()