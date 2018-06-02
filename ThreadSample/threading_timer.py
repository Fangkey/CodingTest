# coding=utf-8
import threading

def hello():
    print 'hello world'

t = threading.Timer(5, hello)		# 5s后调用hello
t.start()