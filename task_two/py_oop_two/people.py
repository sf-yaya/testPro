"""
python实战练习2
课后作业2
用类和面向对象的思想，“描述”生活中任意接触到的东西（比如动物、小说里面的人物，不做限制，随意发挥），数量为5个
"""


# 定义一个可爱的小姐姐
class People:
    # 定义变量
    lovely = "我很可爱"
    hand = "我有一双手"
    feet = "我有一双大长腿"
    eye = "我是单眼皮"

    # 定义一个吃的方法
    def eat(self):
        print("我是一个小吃货")

    # 定义一个跑的方法
    def run(self):
        print("我跑的很快")


# 类的实例化
pp = People()
# 调用类中的方法及属性
pp.run()
pp.eat()
print(pp.lovely)
print(pp.eye)
