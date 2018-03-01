import gevent
import greenlet


def callback(event, args):
    print(event, args[0], '===:>>>>', args[1])


def foo():
    print('Running in foo')
    gevent.sleep(0)
    print('Explicit context switch to foo again')


def bar():
    print('Explicit context to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')


# def test():
#     print('Explicit context to test')
#     gevent.sleep(0)
#     print('Implicit context switch back to test')


print('main greenlet info: ', greenlet.greenlet.getcurrent())
# print('hub info', gevent.get_hub())
oldtrace = greenlet.settrace(callback)

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
])
# gevent.joinall([
#     gevent.spawn(foo),
#     gevent.spawn(bar),
#     gevent.spawn(test)
# ])
# print('All done')
greenlet.settrace(oldtrace)
"""
每一次waiter.get()都会switch到hub
"""
