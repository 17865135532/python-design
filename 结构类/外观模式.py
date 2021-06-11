#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
外观模式： 隐藏系统的复杂性， 并向客户端提供了一个客户端可以访问系统的接口。这种类型的设计属于结构性模式， 它向现有的系统添加一个接口，来隐藏系统的复杂性
解决问题：
    减低访问复杂系统的内部子系统复杂度， 简化客户端与之的接口
"""


class A1():
    def run(self):
        print(f"run: {self.__module__}")


class A2():
    def run(self):
        print(f"run: {self.__module__}")


class A3():
    def run(self):
        print(f"run: {self.__module__}")


class SumFunc():
    def __init__(self):
        self.a1 = A1()
        self.a2 = A2()
        self.a3 = A3()

    def runAll(self):
        self.a1.run()
        self.a2.run()
        self.a3.run()


def main():
    SumFunc().runAll()


if __name__ == '__main__':
    main()
