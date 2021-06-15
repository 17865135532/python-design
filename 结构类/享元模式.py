#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
享元模式主要用于尖山创建对象的数量， 以减少内存占用 和 提高性能。 属于 结构型模式
解决问题：
    有大量对象时， 有可能会造成内存溢出，我们把其中共同的部分抽象出来 如果有相同的业务请求， 直接返回在内存中已有的对象。 避免重复创建。
何时使用：
    1、系统中有大量对象
    2、这些对象消耗大量内存
    3、这些对象的状态大部分可以外部化
    4、这些对象可以按照内蕴状态分为很多组，当把外蕴对象从对象中剔除出来时， 每一组对象都可以用一个对象来消耗
    5、系统不依赖于这些对象身份， 这些对象是不可分辨的。
优点：
    大大减少对象的创建，降低系统的内存消耗， 使效率提高
实例：
#对应客户顾客类
class Customer:
    name=""
    def __init__(self,name):
        self.name=name
    def order(self,coffee_name):
        print("%s ordered a cup of coffee:%s"%(self.name,coffee_name))
        return Coffee(coffee_name)

按照一般的处理流程，用户在网上预订咖啡，其代表用户的Customer类中生成一个Coffee类，直到交易流程结束。整个流程是没有问题的。
但是在高并发的情况下，也就是说单位时间内购买咖啡的用户越来越多，生成的咖啡实例就会越来越多，系统资源消耗越来越大
避免重复实例的出现，是节约系统资源的一个突破口。引入咖啡工厂类
"""

# 创建coffee实例

class Coffee:
    name = ""
    price = 0.0

    def __init__(self, name):
        self.name = name
        self.price = len(name) # price 由 name 来查询获得

    def show(self):
        print(f"Coffee name: {self.name}  price: {self.price}")


# 生产 Coffee 的 factory
class CoffeeFactory():
    coffee_dict = {}

    def getCoffee(self, name):
        if self.coffee_dict.__contains__(name) == False:
            self.coffee_dict[name] = Coffee(name)
        return self.coffee_dict[name]

    def getCoffeeCount(self):
        return len(self.coffee_dict)

class Customer:
    """
        客户
    """
    coffee_factory = ""
    name = ""

    def __init__(self, name, coffee_factory):
        self.name = name
        self.coffee_factory = coffee_factory

    def order(self, coffee_name):
        print(f"orderd: {self.name} a cup of coffee: {coffee_name}")
        return self.coffee_factory.getCoffee(coffee_name)



def main():
    # 模拟多人下咖啡订单
    coffee_factory = CoffeeFactory()
    customer_1 = Customer(name="A Client", coffee_factory=coffee_factory)
    customer_2 = Customer(name="B Client", coffee_factory=coffee_factory)
    customer_3 = Customer(name="C Client", coffee_factory=coffee_factory)
    c1_capp = customer_1.order("cappuccino1")
    c1_capp.show()
    c2_capp = customer_1.order("cappuccino1")
    c2_capp.show()
    c3_capp = customer_1.order("cappuccino1")
    c3_capp.show()
    # c2_mocha = customer_2.order("mocha")
    # c2_mocha.show()
    # c3_capp = customer_3.order("cappuccino")
    # c3_capp.show()
    print("Num of Coffee Instance:%s" % coffee_factory.getCoffeeCount())



if __name__ == '__main__':
    main()