# coding=utf-8
import threading
import time


class SetGlobalVariableThread(threading.Thread):
    def __init__(self, thread_name):
        super(SetGlobalVariableThread, self).__init__(name=thread_name)

    def run(self):
        global x
        x += 1
        time.sleep(2)
        print x


x = 0
threads = []
for i in range(10):
    threads.append(SetGlobalVariableThread(i))

for t in threads:
    t.start()
