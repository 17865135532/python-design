#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
    中介者模式
    实现：中介
    系统A 系统B 系统C
        中介者
          |
          |

关键代码：对象 Colleague 之间的通信封装到一个类中单独处理。
"""


# 后台定义
class Colleague():
    mediator = None

    def __init__(self, mediator):
        self.mediator = mediator


class PurcjaseColleague(Colleague):
    ...


class WareHouseColleague(Colleague):
    ...


class SalesColleague(Colleague):
    ...


# 中介者实现
class ABStracMediator():
    purchase = ''
    sales = ''
    warehouse = ''

    def setPurchase(self, purchase):
        self.purchase = purchase

    def setWareHouse(self, warehouse):
        self.warehouse = warehouse

    def setSales(self, sales):
        self.sales = sales

    def execute(self, content, num):
        ...


class StockMediator(ABStracMediator):
    def execute(self, content, num):
        # 根据 content 来 实现对应逻辑功能
        ...


def main():
    ...


if __name__ == '__main__':
    main()
