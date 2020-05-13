"""
python实战练习2
课后作业2
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""


# 定义一个汽车类
class Car:
    # 定义变量
    wheel = 4
    steering_wheel = "我是方向盘，可以调整方向"
    horn = "我是喇叭，可以发出嘀嘀嘀的声音！"

    # 定义run的方法
    def run(self, wheel):
        print("我有{}个轮子，我跑的很快".format(wheel))

    # 定义一个方向的方法
    def direction(self, horn):
        print("{}".format(horn))
    # 定义左转的方法


# 实例化类
c = Car()
# 调用类中的方法、属性
c.run(c.wheel)
c.direction(c.horn)


#  定义一本书类
class Book:
    # 定义变量、属性
    page = 100
    colour = "红色"

    # rectangle = "我是长方形"
    # 定义打开的方法
    def open(self, page):
        print("请打开第{}页".format(page))

    # 定义关上的方法
    def close(self):
        print("请关上书本休息一会儿吧！")

    # 定义阅读的方法
    def read(self, colour):
        print("我在看一本{}的书".format(colour))


# 实例化类
bk = Book()
# 调用类中的属性、方法
bk.open(bk.page)
bk.close()
bk.read(bk.colour)


# 定义一个电饭锅类
class RiceCooker:
    # 定义变量
    size = "4升"
    shape = "球形"

    # 定义函数、方法
    def cook_rice(self, size):
        print("我的容量很多大,{}，可以煮很多米饭".format(size))

    def stew_soup(self):
        print("我煲的汤好香呀！")


# 实例化类
rc = RiceCooker()
# 调用类的属性、方法
rc.cook_rice(rc.size)
rc.stew_soup()
rc.shape
