def countdown(n):
    print('Counting down from ', n)
    while n > 0:
        yield n
        n -= 1


"""
>>> from src.test_generator import countdown
>>> x = countdown(10)
>>> x
<generator object countdown at 0x00000175FE507A98>
>>> next(x)
Counting down from  10
10
>>> next(x)
9
...
>>> next(x)
1
>>> next(x)
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration
"""


def grep(pattern, lines):
    for line in lines:
        if pattern in line:
            yield line


if __name__ == '__main__':
    text = ['python rocks', 'pth rck', 'python3.5', 'pp test']
    pattern = 'python'
    for line in grep(pattern, text):
        print(line)
