#!/usr/bin/python
# -*- encoding: utf-8 -*-

# 装饰器模式实现

def singleton(cls):
    _isinstance = {}

    def _singleton(*args, **kwargs):
        if cls not in _isinstance:
            _isinstance[cls] = cls(*args, **kwargs)
        return _isinstance

    return _singleton


@singleton
class ABC(object):
    a = 1

    def __init__(self, x):
        self.x = x
        print(f"这是A的类的初始化方法: {self.x}")


def main():
    for i in range(10):
        print(f"i: {i} :{ABC(i)}")


if __name__ == '__main__':
    main()
