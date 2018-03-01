"""
greenlet只提供协程本身,要在协程间切换调度必须你在程序中手动来进行
API:
    greenlet(run=None, parent=None): create a greenlet instance
    greenlet.getcurrent
Attributes and methods:
    gr.parent: 每一个协程都有一个父协程,当前协程结束后会回到父协程中执行,该属性默认是创建该协程的协程
    gr.run: 该属性是协程实际运行的代码. run方法结束了,那么该协程也就结束了.
    gr.switch(*args, **kwargs): 切换到gr协程, 开始/恢复执行run.
    gr.throw(): 切换到gr协程,接着抛出一个异常.


ref:
https://greenlet.readthedocs.io/en/latest/
https://github.com/python-greenlet/greenlet/blob/master/greenlet.h
https://github.com/python-greenlet/greenlet/blob/master/greenlet.c

每个greenlet都只是heap中的一个python object(PyGreenlet):
typedef struct _greenlet {
 PyObject_HEAD
 char* stack_start;
 char* stack_stop;
 char* stack_copy;
 intptr_t stack_saved;
 struct _greenlet* stack_prev;
 struct _greenlet* parent;
 PyObject* run_info;
 struct _frame* top_frame;
 int recursion_depth;
 PyObject* weakreflist;
 PyObject* exc_type;
 PyObject* exc_value;
 PyObject* exc_traceback;
 PyObject* dict;
} PyGreenlet;

Stack layout for a greenlet:
               |     ^^^       |
               |  older data   |
               |               |
  stack_stop . |_______________|
        .      |               |
        .      | greenlet data |
        .      |   in stack    |
        .    * |_______________| . .  _____________  stack_copy + stack_saved
        .      |               |     |             |
        .      |     data      |     |greenlet data|
        .      |   unrelated   |     |    saved    |
        .      |      to       |     |   in heap   |
 stack_start . |     this      | . . |_____________| stack_copy
               |   greenlet    |
               |               |
               |  newer data   |
               |     vvv       |

"""
from greenlet import greenlet


def test1(x, y):
    z = gr2.switch(x+y)
    print(z)


def test2(u):
    print(u)
    gr1.switch(42)


gr1 = greenlet(test1)
gr2 = greenlet(test2)
gr1.switch("hello", " world")

"""
hello world
42
"""

"""
greenlet通过switch在greelet间自由切换传值
Generator based coroutine通过yield归还控制权到主调用者，sub-generator无法互相传值，只能通过主调用者传递
"""

# def foo():
#     print('foo')
#     x, y = yield
#     print('foo')
#     z = b.send(x + y)
#     print('foo')
#     print(z)
#
#
# def bar():
#     print('bar')
#     u = yield
#     print('bar')
#     print(u)
#     f.send(42)
#     print('bar')
#
#
# f = foo()
# b = bar()
# f.send(None)
# b.send(None)
# f.send(('hello', ' world'))
"""
foo
bar
foo
bar
hello world
Traceback (most recent call last):
  File "D:/Eigen/ansyc_io_demo/src/test.py", line 23, in <module>
    f.send(('hello', ' world'))
  File "D:/Eigen/ansyc_io_demo/src/test.py", line 5, in foo
    z = b.send(x + y)
  File "D:/Eigen/ansyc_io_demo/src/test.py", line 15, in bar
    f.send(42)
ValueError: generator already executing
"""