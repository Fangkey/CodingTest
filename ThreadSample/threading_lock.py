# coding=utf-8
import threading

lock = threading.Lock()		# Lock对象
lock.acquire()				# 正常
lock.acquire()  			# 产生了死琐,程序一直阻塞在这里。
lock.release()
lock.release()

rLock = threading.RLock()  	# RLock对象
rLock.acquire()				# 正常
rLock.acquire()				# 可重入锁对象,在同一线程内，程序不会堵塞。
rLock.release()				# 释放
rLock.release()				# 释放