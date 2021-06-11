#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
使用一个一个简单对象构建一个复杂对象

解决问题：
    主要解决在软件系统中，有时候面临着”一个复杂对象“的创建工作， 其通常由各个部分的子对象用一定的算法构成；由于需求的变化这个复杂对象的各个部分经常面临着剧烈的变化，
    但是将他们组和在一块相对稳定
何时使用：
    一个复杂的功能下， 拆解多个子功能， 部分功能稳定， 部分功能变化较大
应用实例： 1、去肯德基，汉堡、可乐、薯条、炸鸡翅等是不变的，而其组合是经常变化的，生成出所谓的"套餐"。 2、JAVA 中的 StringBuilder。
优点： 1、建造者独立，易扩展。 2、便于控制细节风险。
缺点： 1、产品必须有共同点，范围有限制。 2、如内部变化复杂，会有很多的建造类。

"""


class Berger():
    """
        汉堡
    """
    name = ""
    price = 0.0

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def setPrice(self, price):
        self.price = price

    def getPrice(self):
        return self.price


class CheeseBurger(Berger):
    """
    奶酪汉堡
    """

    def __init__(self):
        self.name = " cheese burger "
        self.price = 12.0


class spicyChickenBurger(Berger):
    """
    香辣汉堡
    """

    def __init__(self):
        self.name = "spicy chicken"
        self.price = 12


class Snack():
    """
        小食类
    """

    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class Chips(Snack):
    """
     薯条
    """

    def __init__(self):
        self.name = "chips"
        self.price = 12.00


class chickenWings(Snack):

    def __init__(self):
        self.name = "chicken wings"
        self.price = 15.00


class Beverage():
    """
    饮料
    """

    name = ""
    price = 0.0
    type = "Beverage"

    def getPrince(self):
        return self.price

    def setPrince(self, price):
        self.price = price

    def getName(self):
        return self.name


class CoCO(Beverage):
    def __init__(self):
        self.name = "coke"
        self.price = 12.00


class Milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 12.00


class Order():
    """
        订单对象，一个订单中包含一份主食，一份小食，一份饮料
    """

    burger = ""
    sanck = ""
    beverage = ""

    def __init__(self, orderBuilder):
        """
            接收 一个 自定义的 orderBuilder 订单创建
        """
        self.burger = orderBuilder.bBurger
        self.sanck = orderBuilder.bSnack
        self.beverage = orderBuilder.bBeverage

    def show(self):
        print(f"{'&' * 10}")
        print(f"Burger: {self.burger.getName()}")
        print(f"sanck: {self.sanck.getName()}")
        print(f"beverage: {self.beverage.getName()}")
        print(f"Burger bf: {self.burger.getPrice()}")
        self.burger.setPrice(price=20)
        print(f"Burger af: {self.burger.getPrice()}")


class OrderBuilder():
    """
        order 建造者
    """
    bBurger = ""
    bSnack = ""
    bBeverage = ""

    def addBurger(self, xburger):
        self.bBurger = xburger
        print(self.bBurger)

    def addSnack(self, xsnack):
        self.bSnack = xsnack

    def addBeverage(self, xbeverage):
        self.bBeverage = xbeverage

    def build(self):
        return Order(self)


def main():
    cb = CheeseBurger()
    # print(cb)
    # print(f"name: {cb.name}")
    # print(f"price: {cb.price}")
    # print(f"price: {cb.getName()}")
    # print(f"price: {cb.getPrice()}")

    order_builder = OrderBuilder()
    # 新增 餐品
    order_builder.addBurger(spicyChickenBurger())
    order_builder.addSnack(Chips())
    order_builder.addBeverage(Milk())
    # 创建 订单
    order_1 = order_builder.build()
    order_1.show()


# 建造者模式：
#

# food: food1, food2, food3
# Order
# OrderBuilder
# order: order1, order2, order3


if __name__ == '__main__':
    main()
