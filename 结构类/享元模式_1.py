#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
享元模式模式的结构
享元模式的主要角色有如下。
    1、抽象享元角色（Flyweight）：是所有的具体享元类的基类，为具体享元规范需要实现的公共接口，非享元的外部状态以参数的形式通过方法传入。
    2、具体享元（Concrete Flyweight）角色：实现抽象享元角色中所规定的接口。
    3、非享元（Unsharable Flyweight)角色：是不可以共享的外部状态，它以参数的形式注入具体享元的相关方法中。
    4、享元工厂（Flyweight Factory）角色：负责创建和管理享元角色。当客户对象请求一个享元对象时，享元工厂检査系统中是否存在符合要求的享元对象，如果存在则提供给客户；如果不存在的话，则创建一个新的享元对象。
"""


# 抽象享元角色
class Coffee:
    name = ""
    price = 0.0

    def __init__(self, name, price=10):
        self.name = name
        self.price = len(name)

    def show(self):
        print(f"Coffee name: {self.name} Price: {self.price}")


class CoffeeFactory():
    coffee_dict = {}

    def getCoffee(self, name):
        if self.coffee_dict.__contains__(name) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def getCoffeeCount(self):
        return len(self.coffee_dict)


# 客户抽象
class Customer:
    name = ""
    coffeeFactory = ""

    def __init__(self, name, coffeeFactory):
        self.name = name
        self.coffeeFactory = coffeeFactory

    def order(self, coffee_name):
        print(f"orderd name: {self.name}  coffeename: {coffee_name}")
        return self.coffeeFactory.getCoffee(coffee_name)


def main():
    coffee_factory = CoffeeFactory()
    customer_1 = Customer("A Client", coffee_factory)
    c1_capp = customer_1.order(coffee_name='mocha')
    print(c1_capp)
    c1_capp.show()


if __name__ == '__main__':
    main()
