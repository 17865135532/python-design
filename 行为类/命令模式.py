#!/usr/bin/python
# -*- encoding: utf-8 -*-
"""
命令模式：是一种数据驱动的设计模式， 它属于行为型模式。 请求以命令的形式包裹在对象中， 并传给调用对象。
    调用对象寻找可以处理该命令的合适的对象， 并将该命令传给响应的对象，该对象执行命令
主要解决：
顺序： 调用者->命令->接受者
关键角色： 1、 真正的命令执行对象 2、 command 命令 3、对象使用的入口
优点： 1、 降低系统的耦合度 2、添加新的命令容易
实例：
    # 主食子系统，凉菜子系统，热菜子系统,后台三个子系统
"""


class BackSys():
    """

    """

    def cook(self, dish):
        ...


class MainFood(BackSys):

    def cook(self, dish):
        print(f"MainFood: {dish}")


class HotDishSys(BackSys):
    def cook(self, dish):
        print(f"HotDishSys: {dish}")


class CoolDishSys(BackSys):

    def cook(self, dish):
        print(f"CoolDishSys: {dish}")


# 前台服务系统与后台系统交互， 我们通过命令的模式来实现
# 实例： 服务员将顾客的点单内容封装成命令， 直接对后台下达命令， 后台接收 对应的指令 来执行指令

# 前台系统构建

class WaiterSys():
    menu_map = dict()
    commandList = []

    def setOrder(self, command):
        print(f"setOrder add command : {command}")
        self.commandList.append(command)

    def cancelOrder(self, command):
        print(f"cancelOrder : {command}")
        self.commandList.remove(command)

    def notify(self):
        for command in self.commandList:
            command.execute()


# 前台系统中的 notify 接口直接调用命令中的 execute 接口 执行命令

class Command():
    receiver = None

    def __init__(self, receiver):
        self.receiver = receiver

    def execute(self):
        pass


class FoodCommand(Command):
    dish = ''

    def __init__(self, receiver, dish):
        self.receiver = receiver
        self.dish = dish

    def execute(self):
        self.receiver.cook(self.dish)


class MainFoodCommand(FoodCommand):
    ...


class CoolDishCommand(FoodCommand):
    ...


class HotDIshCommand(FoodCommand):
    ...


"""
    Command类 是比较通过的类， FoodCommand 类是本例中涉及的类， 相比于Command类进行了一定的改造
    由于后台系统中的执行函数是cook， 因而在 FoodCommand类中直接将 execute接口实现
    如果后台系统执行函数不同， 需要在三个子命令系统中实现 execute 接口
    这样，后台三个命令类就可以直接继承，不用进行修改了。
"""


# 菜单类辅助业务
class menu_map():
    menu_map = dict()

    def loadMenu(self):
        """
            加载菜单
        """
        self.menu_map["hot"] = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Sauteed Snow Peas"]
        self.menu_map["cool"] = ["Cucumber", "Preserved egg"]
        self.menu_map["main"] = ["Rice", "Pie"]

    def isHot(self, dish):
        if dish in self.menu_map["hot"]:
            return True
        return False

    def isCool(self, dish):
        if dish in self.menu_map["cool"]:
            return True
        return False

    def isMain(self, dish):
        if dish in self.menu_map["main"]:
            return True
        return False


def main():
    dish_list = ["Yu-Shiang Shredded Pork", "Sauteed Tofu, Home Style", "Cucumber", "Rice"]  # 顾客点的菜
    # 前台
    waitersys = WaiterSys()
    # 对应后台
    main_food_sys = MainFood()
    cool_food_sys = CoolDishSys()
    hot_food_sys = HotDishSys()
    # 菜单
    menu = menu_map()
    menu.loadMenu()
    #
    for dish in dish_list:
        if menu.isMain(dish):
            cmd = CoolDishCommand(cool_food_sys, dish)
            print(f"cmd: {cmd}")
        elif menu.isMain(dish):
            cmd = MainFoodCommand(main_food_sys, dish)
        elif menu.isHot(dish):
            cmd = HotDIshCommand(hot_food_sys, dish)
        else:
            continue
        waitersys.setOrder(command=cmd)
    waitersys.notify()


if __name__ == '__main__':
    main()
