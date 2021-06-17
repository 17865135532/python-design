#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
观察者模式：当对象间存在一对多的关系时， 则使用观察者模式，
    比如： 当一个对象被修改时，则会自动通知依赖它的对象， 观察者模式属于行为型模式
意图： 定义对象间的一种一对多的依赖关系时， 当一个对象状态改变之后， 所有依赖的对象都得到通知并自动更新
主要解决：一个对象状态改变给其他对象通知的问题，而且要考虑到易用和低耦合，保证高度的协作
"""

"""
    举例： 门面模式 三个传感器类的结构。 报警器， 洒水器， 拨号器 都是观察烟雾传感器的 情况来做反应的， 因而 三个是 观察者， 烟雾传感器是被观察对象
    根据分析 将三个类提取共性，泛化出”观察者‘类，并 构造 被观察者。
"""


class AlarmSensor:
    def run(self):
        print(f"AlarmSensor")


class WaterSprinker:
    def run(self):
        print("WaterSprinker")


class EmergencyDiler:
    def run(self):
        print(EmergencyDiler.__name__)
        print("Dial 119...")



def main():
    ...


if __name__ == '__main__':
    main()
