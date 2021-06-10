#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    涉及单一的类， 该类负责创建自己的对象， 确保只有单个对象被创建
    解决问题：一个全局使用的类频繁的创建与销毁
    注意：
        单例类只有一个实例
        单例类必须创建自己的唯一实例
        单例类必须给所有其他对象提供这一实例
"""

import time
import threading


class Sinleton(object):
    # __new__ 实现
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Sinleton, cls)
            cls._instance = orig.__new__(cls, *args, **kwargs)
        return cls._instance


class Bus(Sinleton):
    lock = threading.RLock()

    def sendData(self, data):
        self.lock.acquire()
        print(f"Sinleton  sendData {data}")
        self.lock.release()

class VisitEntity(threading.Thread):

    my_bus = ""
    name = ""

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def run(self):
        self.my_bus = Bus()
        self.my_bus.sendData(self.name)


def main():
    for i in range(5):
        print(f"entity num: {i} is begging run ")
        my_entity = VisitEntity()
        my_entity.setName(f"Entity_{i}")
        my_entity.run()


if __name__ == '__main__':
    main()
