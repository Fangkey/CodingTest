# coding=utf-8
import thread
import time

secs = [4, 2]


def loop(nloop, sec, lock_obj):
    print 'satrt loop:%s at:[%s]' % (nloop, time.ctime())
    time.sleep(sec)
    lock_obj.release()  # 释放锁


def main():
    """主线程使用锁来控制子线程"""
    print 'starting at:', time.ctime()
    lock_objs = []
    nloops = range(len(secs))

    # 分配锁对象
    for i in nloops:
        lock = thread.allocate_lock()       # 分配一个LockType类型的锁对象
        lock.acquire()                      # 尝试获取锁对象
        lock_objs.append(lock)

    # 创建线程
    for i in nloops:
        thread.start_new_thread(loop, (i,               # thead编号,0-1
                                       secs[i],         # sleep时间
                                       lock_objs[i]))   # 分配的锁对象

    # 确保所有锁对象都释放了主线程才退出
    for i in nloops:
        while lock_objs[i].locked():
            pass

    print 'all done at:', time.ctime()


if __name__ == '__main__':
    main()