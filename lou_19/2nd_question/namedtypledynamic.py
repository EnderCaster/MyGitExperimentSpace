#!/usr/bin/env python
# -*- utf-8 -*-
"""介绍
前面的挑战我们实现了一个 NamedTuple 类，它支持通过别名去访问内部元素。但它有个问题是，无论我们传递给构造函数的参数是什么样的，创建出来的对象类型都是一样的。比如通过”NamedTuple([1, 2], ['x', 'y'])“创建的对象代表的是一个二维平面的点，我们希望它的类型是 Point，打印出来是”Point(x=1, y=2)“。本次挑战需要实现一个函数，调用该函数将返回一个动态生成的命名 Tuple 类。

目标
功能点
模块文件保存路径为 /home/shiyanlou/namedtupledynamic.py
模块内实现一个 named_tuple 函数，其参数依次为 typename 和 field_names，分别用于传递要生成的类名和数据别名
动态生成的命名 Tuple 类需要支持通过位置索引和别名属性两种方式去获取数据
动态生成的命名 Tuple 类 repr 输出格式类似于”Point(x=1, y=2)“，其中 Point 为类名，x、y 是别名，1、2 是数据。
不能使用 Python 标准库里的实现，代码里不能出现 namedtuple 相关字样
答案验证
named_tuple 函数需要能通过以下单元测试。该单元测试仅做参考，不作为验证标准。

运行单元测试用的是实验环境里的 python3，具体版本为 3.5

import unittest

from namedtupledynamic import named_tuple


class TestNamedTupleDynamic(unittest.TestCase):
    def test_features(self):
        Point = named_tuple('Point', ['x', 'y'])
        p = Point(1, 2)

        self.assertEqual(p[0], 1)
        self.assertEqual(p[1], 2)

        self.assertEqual(p.x, 1)
        self.assertEqual(p.y, 2)

        self.assertEqual(repr(p), 'Point(x=1, y=2)')

提示语
动态类的代码通过一个类模板来生成，然后使用 exec 函数执行该代码来动态生成一个类
别名属性可在类模板里通过 property 方式来定义
知识点
运行时代码生成和执行
"""
