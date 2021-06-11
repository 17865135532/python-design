#!/usr/bin/python
# -*- encoding: utf-8 -*-

"""
抽象工厂模式
    抽象工厂模式 是 围绕一个超级工厂创建其他工厂，
    该超级工厂又称为其他工厂的工厂， 在抽象工厂模式中，接口是负责创建一个相关对象的工厂，不需要显式指定它们的类。每个生成的工厂都能按照工厂模式提供对象。

解决问题：解决接口选择的问题
        隐藏我们底层接口， 选择性的开放部分接口
何时使用：系统的产品有多于一个的产品族，而系统只消费其中某一族的产品。
举例：
    饭店餐饮
                  |—— 食品1-{食品属性1 ...}
                  |
    定义基础食品类型|—— 食品2-{食品属性1 ...}
                  |
                  |—— 食品3-{食品属性1 ...}

                      |—— 食品1创建
                      |
    定义创建食品生产基础类 —— 食品2创建
                      |
                      |—— 食品3创建
"""


class Burger():
    name = ""
    type = "Burger"
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class cheseBurger(Burger):

    def __init__(self):
        self.name = " chese Burger "
        self.price = 10.0


class spicyChickenBurger(Burger):

    def __init__(self):
        self.name = " chicken  Burger "
        self.price = 15.0


# ------------------------------------------------

class Snack():
    name = ""
    price = 0.0
    type = "SNACK"

    def getPrice(self):
        return self.price

    def setPice(self, price):
        self.price = price

    def getName(self):
        return self.name


class Chips(Snack):

    def __init__(self):
        self.name = "chips"
        self.price = 6.0


class chickenWings(Snack):

    def __init__(self):
        self.name = "chicken Wings"
        self.price = 12.0


class Beverage():
    """
        饮料
    """
    name = ""
    price = 0.0
    type = "BEVERAGE"

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name


class Coke(Beverage):

    def __init__(self):
        self.name = "coke"
        self.price = 4.0


class Milk(Beverage):
    def __init__(self):
        self.name = "milk"
        self.price = 5.0


class foodFactory():
    """
        foodFactory 抽象 工厂类， 其他类继承foodFactory 来产生具体的工厂类
    """
    type = ""

    def createFood(self, foodclass):
        print(f"foodclass: {foodclass}")
        print(f"foodclass: {foodclass.type}")
        return foodclass()


class burgerFactory(foodFactory):
    """
        food1
    """

    def __init__(self):
        self.type = "BURGER"


class snackFactory(foodFactory):
    """
        food2
    """

    def __init__(self):
        self.type = "SNACK"


class BeverageFactory(foodFactory):
    """
       food3
    """

    def __init__(self):
        self.type = "BEVERAGE"


def main():
    burger_factory = burgerFactory()
    snack_factory = snackFactory()
    beverage_factory = BeverageFactory()

    # haburger
    chese_burger = burger_factory.createFood(cheseBurger)
    print(f"chese_burger: {chese_burger}")
    print(f"name: {chese_burger.getName()}  price: {chese_burger.getPrice()}")

    # snack
    snack = snack_factory.createFood(Chips)
    print(f"snack: {snack}")
    print(f"name: {snack.getName()}  price: {snack.getPrice()}")

    # milk
    beverage = beverage_factory.createFood(Milk)
    print(f"beverage: {beverage}")
    print(f"mike name: {beverage.getName()}  milk price: {beverage.getPrice()}")


if __name__ == '__main__':
    main()
