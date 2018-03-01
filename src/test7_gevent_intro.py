import gevent
# from gevent.monkey import patch_time
# patch_time()
# import time


def foo():
    while True:
        print('foo is running')
        gevent.sleep(0.5)
        # time.sleep(0.5)


def bar():
    while True:
        print('bar is running')
        gevent.sleep(0.5)


tasks = [gevent.spawn(foo), gevent.spawn(bar)]
gevent.joinall(tasks)
"""
foo is running
bar is running
foo is running
bar is running
foo is running
...
"""
