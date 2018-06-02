# coding=utf-8
import thread
import time

def loop0():
    print 'start loop0 at:', time.ctime()
    time.sleep(4)
    print 'end loop0 at:', time.ctime()


def loop1():
    print 'start loop1 at:', time.ctime()
    time.sleep(2)
    print 'end loop1 at:', time.ctime()

def main():
    print 'all loops at:', time.ctime()
    t1 = thread.start_new_thread(loop0, ())
    t2 = thread.start_new_thread(loop1, ())
    # why sleep 6s？
    time.sleep(6)
    print 'all loops done at:', time.ctime()


if __name__ == '__main__':
    main()