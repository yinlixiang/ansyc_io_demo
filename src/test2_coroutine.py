"""
generators are completely independent from each other:
yield will 'pause' a generator
next()/send() will resume a paused generator
generator只有在yield处才能挂起，将程序控制转给调用者；
而调用者通过next/send也只能和在yield处挂起的generator进行交互。
这就意味着控制权只能在generator和调用者之间轮换，而且是在yield处进行轮换，
如果多个generator之间交换数据，那么只能通过主调者进行中转。
"""


def grep_first(pattern):
    print('Looking for {}'.format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print(line)

"""
g = grep_first('python')
next(g) # g.send()
g.send('test')
g.send('python rocks!')
"""


def coroutine(func):
    def start(*args, **kwargs):
        cr = func(*args, **kwargs)
        cr.__next__()     # next(cr) to start generator, stand by at yield
        return cr
    return start


@coroutine
def grep_second(pattern):
    print('Looking for {}'.format(pattern))
    while True:
        line = (yield)
        if pattern in line:
            print(line)


@coroutine
def grep(pattern):
    print('Looking for {}'.format(pattern))
    try:
        while True:
            line = (yield)
            if pattern in line:
                print(line)
    except GeneratorExit:
        print('closed')


if __name__ == '__main__':
    g = grep('python')
    g.send('test')
    g.send('test py')
    g.send('python generators rock!')
    # g.throw(RuntimeError)
    g.close()
