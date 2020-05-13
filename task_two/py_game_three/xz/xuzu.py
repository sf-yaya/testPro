"""
定义一个XuZhu类，继承于童姥。虚竹宅心仁厚不想打架。所以虚竹只有一个read（念经）的方法。每次调用都会打印“罪过罪过”
加入模块化改造

"""
# 定义一个类
from task_two.py_game_three.tl.tonglao import TongLao


class XuZhu(TongLao):
    # 初始化变量
    # def __init__(self):
    #  aa=1

    def read(self):
        print("罪过罪过")


# 实例化类
xz = XuZhu()
# 调用方法
xz.read()
# 调用父类的方法
xz.fight_zms(1000, 300)
xz.see_people(xz.name)
