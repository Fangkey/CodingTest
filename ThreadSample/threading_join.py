# coding=utf-8
import time
import threading

def foo(sec):
    print '%s starting..' % sec
    time.sleep(sec)
    print '%s end..' % sec


def main():
    threads = []
    for i in range(5):
        t = threading.Thread(target=foo, args=(i,))  # 创建Thread实例并传参
        threads.append(t)

    for i in threads:
        i.start()   # 启动所有

    for i in threads:
        i.join()    # 等待结束

if __name__ == '__main__':
    main()