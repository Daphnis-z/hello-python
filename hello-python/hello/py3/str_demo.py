#!/usr/bin/python3
"""
@File:   str_demo.py
@Author: daphnis
@Time:   2020-11-21 17:21:25
@Desc:   记录一些特殊的字符串相关用法
"""
import random

people = 'daphnis'
print(f'hello {people}')
print('hello {}'.format(people))
print('hello %s' % people)

# 生成固定长度的数字，长度不够在最左边补 0
num = int(random.uniform(100, 10000))
print(str(num).zfill(5))
