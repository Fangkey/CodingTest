# coding=utf-8
import threading
import time
from collections import deque

class ThreadProducer(threading.Thread):
    def __init__(self, cond_obj):
        super(ThreadProducer, self).__init__()
        self.cond = cond_obj
        self.task_list = deque([])

    def produce(self, task):
        self.cond.acquire()
        print "producer append " + str(task) + "|"
        self.task_list.append(task)
        print "producer len " + str(len(self.task_list))
        self.cond.notify()
        self.cond.release()


    def run(self):
        cnt = 0
        while True:
            self.produce(cnt)
            cnt += 1
            #time.sleep(0.1)

class ThreadConsumer(threading.Thread):
    def __init__(self, name, cond_obj, producer_obj):
        super(ThreadConsumer, self).__init__(name=name)
        self.cond = cond_obj
        self.producer = producer_obj

    def consume(self):
        self.cond.acquire()
        print self.name + " Before Len: " + str(len(self.producer.task_list)) + "|"
        if len(self.producer.task_list) == 0:
            print self.name + " waiting.|"
            print self.cond.wait()
            print self.name + " quit waiting.|"
        print self.name + " After Len: " + str(len(self.producer.task_list)) + "|"
        print self.name + " consuming.|"
        task = self.producer.task_list.popleft()
        print str(task) + "|"



        # important, don't know why there must be a while
        # 正解：如果用户没有传入锁（lock）对象，condition类的构造器创建一个可重入锁（RLock），这个锁将会在调用acquire()和release()时使用。
        # class _Condition(_Verbose):
        #     def __init__(self, lock=None, verbose=None):
        #         _Verbose.__init__(self, verbose)
        #         if lock is None:
        #             lock = RLock()
        #         self.__lock = lock
        # 似乎还是不对，改成Lock对象依然出错

        # while True:
        #     if self.producer.task_list:
        #         print self.name + " consuming.|"
        #         task = self.producer.task_list.popleft()
        #         print str(task) + "|"
        #         break
        #     print self.name + " waiting.|"
        #     self.cond.wait()
        self.cond.release()

    def run(self):
        while True:
            self.consume()
            #time.sleep(3)


if __name__ == "__main__":
    cond_lock = threading.Lock()
    cond = threading.Condition(lock=cond_lock)
    producer = ThreadProducer(cond)
    consumer_list = []
    for i in range(0, 10):
        name = "con_" + str(i)
        consumer = ThreadConsumer(name, cond, producer)
        consumer_list.append(consumer)
        consumer.start()

    producer.start()


