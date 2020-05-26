import random
import time

player_list =  ['【狂血战士】','【森林箭手】','【光明骑士】','【独行剑客】','【格斗大师】','【枪弹专家】']
enemy_list = ['【暗黑战士】','【黑暗弩手】','【骷髅骑士】','【嗜血刀客】','【首席刺客】','【陷阱之王】']

player = random.sample(player_list,3)
enemy = random.sample(enemy_list,3)

player_info = {}
enemy_info = {}

def born_role():
    for i in range(3):
        life = random.randint(100, 180)
        attack = random.randint(30, 50)
        return life, attack


def show_role():
    for i in range(3):
        player_info[player[i]] = born_role()
        enemy_info[enemy[i]] = born_role()



    print('----------------- 角色信息 -----------------')
    print('你的人物：')
    for i in range(3):
        print(f'{player[i]}\n血量：{player_info[player[i]][0]}\n攻击力：{player_info[player[i]][1]}')
        print('--------------------------------')
        time.sleep(0.5)

    print('\n你的敌人：')
    for i in range(3):
        print(f'{enemy[i]}\n血量：{enemy_info[enemy[i]][0]}\n攻击力：{enemy_info[enemy[i]][1]}')
        print('--------------------------------')
        time.sleep(0.5)
    input('轻按回车继续。\n')

show_role()



def order():
    global show_num
    order_num = {}
    for i in range(3):
        order = int(input(f'你希望你的角色： {player[i]}第几个出场呢？  '))
        order_num[order] = player[i]

    show_num = []
    for i in range(1,4):
        show_num.append(order_num[i])

    print('以下是我方的出场的顺序：\n')


    for i in range(3):
        print(show_num[i])

    print('以下是敌方的出场顺序：\n')

    for i in range(3):
        print(enemy[i])



order()

def pk_role():
    round = 1
    score = 0
    for i in range(3):
        player_name = show_num[i]
        enemy_name = enemy[i]


#
# def show_role(player,enemy,player_life,player_attack,enemy_life,enemy_attack):
#     print('{}\n血量: {}\n攻击力: {}'.format(player,player_life,player_attack))
#     print('--------------------------------')
#     time.sleep(1)
#     print('{}\n血量: {}\n攻击力: {}'.format(enemy, enemy_life, enemy_attack))
#     print('--------------------------------')
#     time.sleep(1)

# def pk_role(player,enemy,player_life,player_attack,enemy_life,enemy_attack):
#     while (player_life >= 0) and (enemy_life >= 0):
#         player_life = player_life - enemy_attack
#         enemy_life = enemy_life - player_attack
#         print('{}发起了攻击，{}目前血量为 {}\n'.format(enemy,player,player_life))
#         time.sleep(0.5)
#         print('{}发起了攻击，{}的目前血量为 {}\n'.format(player,enemy,enemy_life))
#         time.sleep(0.5)
#         print('--------------------------------')
#         time.sleep(1)
#         show_result(player,enemy,player_life,enemy_life)

def show_result(player,enemy,player_life,enemy_life,player_win=0,enemy_win=0):
    if (player_life > 0) and (enemy_life <= 0):
        print('{}获胜\n'.format(player))
        player_win = player_win + 1
        time.sleep(1)
    elif (player_life <= 0) and (enemy_life > 0):
        print('{}赢了\n'.format(enemy))
        enemy_win = enemy_win + 1
        time.sleep(1)
    else:
        print('不好，同归于尽了\n')
        time.sleep(1)

def main(player,enemy,player_life,player_attack,enemy_life,enemy_attack):
    show_role(player, enemy, player_life, player_attack, enemy_life, enemy_attack)
    pk_role(player, enemy, player_life, player_attack, enemy_life, enemy_attack)
    show_result(player,enemy,player_life,enemy_life)


