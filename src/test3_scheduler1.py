from queue import Queue


# A Task is a wrapper around a coroutine
class Task(object):
    taskid = 0

    def __init__(self, target):
        Task.taskid += 1
        self.tid = Task.taskid
        self.target = target
        self.sendval = None

    def run(self):
        return self.target.send(self.sendval)


class Scheduler(object):
    def __init__(self):
        self.ready = Queue()
        self.taskmap = {}

    def new(self, target):
        newtask = Task(target)
        self.taskmap[newtask.tid] = newtask
        self.schedule(newtask)
        return newtask.tid

    def schedule(self, task):
        self.ready.put(task)

    def exit(self, task):
        print('Task {} terminated'.format(task.tid))
        del self.taskmap[task.tid]

    def mainloop(self):
        while self.taskmap:
            task = self.ready.get()
            try:
                result = task.run()
            except StopIteration:
                self.exit(task)
                continue
            self.schedule(task)


if __name__ == '__main__':
    import time

    def foo():
        for i in range(3):
            time.sleep(0.5)
            print('foo running')
            yield

    def bar():
        # while True:
        for i in range(5):
            time.sleep(0.5)
            print('bar running')
            yield

    sched = Scheduler()
    sched.new(foo())
    sched.new(bar())
    sched.mainloop()

"""
yield is a trap!
Each task runs until it hits the yield. At this point, the scheduler regains control
and switches to the other ready task
"""
