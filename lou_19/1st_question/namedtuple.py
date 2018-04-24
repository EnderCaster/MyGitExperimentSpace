#!/usr/bin/env python
# -*- utf-8 -*-
"""介绍
tuple 是 Python 的一种不可变数据类型，用于列表数据一旦初始化就不会再修改的场景。tuple 只能通过位置索引去访问里面的元素，但有时候我们需要给每个元素取个别名，以便通过别名去获取对应的元素。本次挑战就是需要大家自己来实现一个简单的命名 Tuple。

目标
功能点
模块文件保存路径为 /home/shiyanlou/namedtuple.py
模块内实现一个 NamedTuple 类，其构造函数接受 iterable 和 fields 两个参数，分别用于传递数据及其对应的别名
NamedTuple 需要支持通过位置索引和别名属性两种方式去获取数据
NamedTuple repr 输出格式类似于”NamedTuple(x=1, y=2)“，其中 x、y 是别名，1、2 是数据。
不能使用 Python 标准库里的实现，代码里不能出现 namedtuple 相关字样
答案验证
NamedTuple 类需要能通过以下单元测试。该单元测试仅做参考，不作为验证标准。

运行单元测试用的是实验环境里的 python3，具体版本为 3.5

import unittest

from namedtuple import NamedTuple


class TestNamedTuple(unittest.TestCase):
    def test_features(self):
        fields = ['x', 'y']
        values = [1, 2]
        nt = NamedTuple(values, fields)

        self.assertEqual(nt[0], 1)
        self.assertEqual(nt[1], 2)

        self.assertEqual(nt.x, 1)
        self.assertEqual(nt.y, 2)

        self.assertEqual(repr(nt), 'NamedTuple(x=1, y=2)')

提示语
NamedTuple 类可以继承于 tuple，但需要注意 tuple 为不可变数据类型，需要覆盖其 __new__ 方法
为了得到想要的 repr 输出，需要实现 __repr__ 方法
知识点
元组
类继承
不可变数据类型

"""
class NamedTuple(tuple):
    pass