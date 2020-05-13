"""
python实战练习2
课后作业2
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""


# 定义一个狗类
class Dog:
    # 定义变量
    feet = 4
    nose = "我的嗅觉很灵敏"
    # 定义一个私有变量、属性
    __style = "我只忠诚于我的主人"

    # 定义一个狗叫的函数、方法
    def call(self):
        print("有小偷的时候我会大声叫")
        # 私有属性在类中调用
        print(self.__style)

    # 定义一个嗅觉的函数、方法
    def smell(self, loyal):
        print("{}".format(loyal))

    # 定义私有属性、私有方法
    def __privet_style(self):
        print("我只属于我的小主人")


# 实例化类
dg = Dog()
# 调用类里面的属性及方法
dg.call()
dg.smell(dg.nose)
print("我有{}条腿，我跑的很快".format(dg.feet))

# 通过name重写的方法可以调到类中的私有属性
# dg._Dog__privet_style()
