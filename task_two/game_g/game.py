"""
一个回合制游戏，每个角色都有hp 和power，hp代表血量，power代表攻击力，hp的初始值为1000，power的初始值为200。
定义一个fight方法：
final_hp = hp-enemy_power
enemy_final_hp = enemy_hp - power
两个hp进行对比，血量剩余多的人获胜
"""
# 定义一个游戏类
class Game:

    # 初始化变量
    def __init__(self, hp, power):
        self.hp = hp
        self.power = power

    # 定义一个fight方法,传入对手的攻击力enemy_power、对手的血量enemy_hp两个参数
    def fight(self, enemy_power, enemy_hp):
        # 对2个hp进行计算
        # 我的最终血量
        final_hp = self.hp - enemy_power
        # 对手的最终血量
        enemy_final_hp = enemy_hp - self.power
        # 两个hp进行对比，血量剩余多的人获胜
        if final_hp > enemy_final_hp:
            print("我赢了")
        elif final_hp == enemy_final_hp:
            print("平局")
        else:
            print("对手赢了")
# 实例化类
gm = Game(1000, 200)
gm.fight(800, 300)
