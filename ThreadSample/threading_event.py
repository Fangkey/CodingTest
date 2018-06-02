# coding=utf-8
import threading


class Thread_A(threading.Thread):
    def __init__(self, event_obj, name):
        """
        @:param event_obj: Event object
        @:param name: thread name
        """
        super(Thread_A, self).__init__(name=name)
        self.event = event_obj

    def run(self):
        while not self.event.is_set():      # test
            print 'Flag False'

        self.event.wait(10)              # wait 10s 等待B的应答, 如果10s后B还没有应答则timeout,自动开闸
        print self.name, 'wait 10s'


class Thread_B(threading.Thread):
    def __init__(self, event_obj, name):
        """
        @:param event_obj: Event object
        @:param name: thread name
        """
        super(Thread_B, self).__init__(name=name)
        self.event = event_obj

    def run(self):
        self.event.set()          # 开始应答A，A接收到应答后被唤醒并执行
        print self.name, 'set'

cond = threading.Event()        # 创建Event实例
t1 = Thread_A(cond, 't1')
t2 = Thread_B(cond, 't2')
t1.start()
t2.start()