#!/usr/bin/python3
"""
@File:   common_demo.py
@Author: daphnis
@Time:   2020-11-22 11:39:16
@Desc:   this is a python3 file
"""
import sys

tec = {'python': 10, 'spark': 8}
print(str(tec))

print(tec.pop('python'))
print(str(tec))

for i in range(2, 8):
    print(i)


# yield 用法，生成器函数 - 斐波那契
# yield 返回的其实是一个迭代器
def fibonacci(n):
    a, b = 0, 1
    cnt = 0
    while cnt <= n:
        yield a
        a, b = b, a + b
        cnt += 1


f = fibonacci(10)  # f 是一个迭代器，由生成器返回生成
while True:
    try:
        print(next(f), end=",")
    except StopIteration:
        sys.exit()
