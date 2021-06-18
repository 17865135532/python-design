#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
中介者模式： 是用来降低多个对象和类之间的通信复杂性，
    这种模式提供了一个中介类。 该类通常处理不同类之间的通信，并支持松耦合，
    使代码易于维护，中介者模式属于行为型模式
主要解决：对象和对象之间存在大量关联关系， 这样势必会导致系统结构变得复杂，我们也需要葛总与之相关联的对象，
    同时作出相应的处理

何时使用：多个类相互耦合，形成网状结构
实例： 各个国家通过 WTO 来互相贸易
       MVC  C（控制器） 就是 M（Model） 和 V（View） 的中介者
"""


# 构造三个子系统，即三个类（在中介者模式中， 这些类叫做同事类）
class Colleage():
    mediator = None

    def __init__(self, mediator):
        self.mediator = mediator


class PurchaseColleage(Colleage):
    """
        购买同事
    """

    def buy_stuff(self, num):
        # 购买
        ...

    def get_notice(self, content):
        print(f"purchase: get notice: {content}")


class WareHouseColleague(Colleage):
    """
        仓库系统
    """
    total = 0
    threshould = 100

    def set_threshould(self, threshould):
        # 设置阈值
        self.threshould = threshould

    def is_enough(self):
        # 是否满足
        if self.total < self.threshould:
            self.mediator.execute('warning', self.total)
            return False
        else:
            return True

    def increase(self, num):
        # increase 增加
        self.total += num
        print(f"warehouse inc: {num}")
        self.mediator.execute('increase', num)
        self.is_enough()

    def decrease(self, num):
        # decrease 减少
        if num > self.total:
            print(f" warehouse: Error stock is not enough {self.total} ")
        else:
            self.total -= num
            print(f"decrease: {num}")
            self.mediator.execute("decrease", num)
        self.is_enough()


class SalesColleague(Colleage):
    """
        销售系统
    """

    def sell_stuff(self, num):
        # 销售系统
        print(f" sell num: {num} ")
        self.mediator.execute("sell", num)

    def get_notice(self, content):
        print(f" Notice: {content} ")


class AbstractMediator():
    """
        中介摘要
    """
    purchase = ""  # 购买
    sales = ""  # 销售
    warehouse = ""  # 仓库

    def setPurchase(self, purchase):
        self.purchase = purchase

    def setWarehouse(self, warehouse):
        self.warehouse = warehouse

    def setSales(self, sales):
        self.sales = sales

    def execute(self, content, num):
        ...


class StockMediator(AbstractMediator):

    def execute(self, content, num):
        """
            中介者模式的 execute 是最重要的方法， 它根据同事类传递的信息， 直接调用各个同事的工作
            在场景类中， 设置仓储阈值为200，先采购300 在卖出12o
        """
        print(f"content : {content}")
        if content == "buy":
            self.warehouse.increase(num)
            self.sales.get_notice(content=content)
        elif content == "increase":
            self.sales.get_notice(f"increase: {content}")
            self.purchase.get_notice(f"increase: {content}")

        elif content == "decrease":
            # 减少
            self.sales.get_notice(f"decrease: {content}")
            self.purchase.get_notice(f"decrease: {content}")

        elif content == "warning":
            self.sales.get_notice(f" stock is low : {num} ")
            self.purchase.get_notice(f"stock is low : {num}")

        elif content == "sell":
            self.warehouse.increase(num=num)
            self.purchase.get_notice(f" sell num: {num} ")

        else:
            ...


def main():
    mobile_mediator = StockMediator()  # 配置
    # 购买
    mobile_purchase = PurchaseColleage(mobile_mediator)
    # 仓储
    mobile_warehouse = WareHouseColleague(mobile_mediator)
    # 销售
    mobile_sales = SalesColleague(mobile_mediator)

    mobile_mediator.setPurchase(mobile_purchase)
    mobile_mediator.setWarehouse(mobile_warehouse)
    mobile_mediator.setSales(mobile_sales)

    mobile_warehouse.set_threshould(200)
    mobile_purchase.buy_stuff(300)
    mobile_sales.sell_stuff(1500)



if __name__ == '__main__':
    main()
