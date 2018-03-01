import gevent
from gevent.hub import get_hub
from gevent.greenlet import getcurrent
# import gevent.monkey
# gevent.monkey.patch_time()
# import time


def test(a):
    print(a)
    gevent.sleep(1)
    print('switch back to task')
    gevent.sleep(1)
    print('switch back to task')
    gevent.sleep(1)
    print('task done')


task = gevent.spawn(test, 'hello')
print(task)
print(task.parent)
h = get_hub()
print(h)
print(h.parent)
g = getcurrent()
print(g)
print(g.parent)
gevent.sleep(1)
# time.sleep(1)
print('switch back to main')
gevent.sleep(1)
print('main done')
gevent.joinall([task])

"""
current greenlet == greenlet.greenlet => Hub => greenlet
current greenlet 也可由Hub调度

gevent.sleep=>hub.wait
"""
