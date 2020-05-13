# 定义一个天山童姥类 ，类名为TongLao
class TongLao:
    # 初试化变量
    def __init__(self):
        self.ph = 100
        self.power = 200
        self.name = ["WYZ", "李秋水", "丁春秋"]

    def see_people(self, name):
        # print("{}".format(name))
        for i in range(len(name)):
            if name[i] == "WYZ":
                print("师弟！！！！")
            if name[i] == "李秋水":
                print("呸，贱人")
            if name[i] == "丁春秋":
                print("叛徒！我杀了你")

    # 天山折梅手方法
    def fight_zms(self, enemy_hp, enemy_power):
        # 调用天山折梅手方法会将自己的武力值提升10倍，血量缩减2倍。
        # 需要传入敌人的hp，power，进行一回合制对打，打完之后，比较双方血：
        final_hp = self.ph % 2 - enemy_power
        enemy_final_hp = enemy_hp - self.power*10
        if final_hp > enemy_final_hp:
            print("我赢了")
        else:
            print("我输了")

# 实力化类
# tl = TongLao()
# tl.fight_zms(100, 500)
# tl.see_people(tl.name)
