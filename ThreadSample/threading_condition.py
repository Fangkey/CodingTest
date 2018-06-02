# coding=utf-8
import threading
import time


class Thread_A(threading.Thread):
    def __init__(self,cond_obj, name):
        """
        @:param cond_obj: Condition object
        @:param name: thread name
        """
        super(Thread_A, self).__init__(name=name)
        self.cond = cond_obj

    def run(self):
        self.cond.acquire()
        self.cond.wait(10)              # wait 10s 等待B的应答, 如果10s后B还没有应答则timeout,自动开闸
        print self.name, 'wait 10s'
        self.cond.release()


class Thread_B(threading.Thread):
    def __init__(self,cond_obj, name):
        """
        @:param cond_obj: Condition object
        @:param name: thread name
        """
        super(Thread_B, self).__init__(name=name)
        self.cond = cond_obj

    def run(self):
        self.cond.acquire()
        self.cond.notify()          # 开始应答A，A接收到应答后被唤醒并执行
        print self.name, 'notify'
        self.cond.release()

cond = threading.Condition()        # 创建Condition实例
t1 = Thread_A(cond, 't1')
t2 = Thread_B(cond, 't2')
t1.start()
t2.start()

# out:
# t2 notify
# t1 wait 10s