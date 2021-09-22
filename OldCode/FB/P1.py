# students = ['小明','小红','小刚']
# students.append('3')
# del students[2]
# print(students)

# students = ['小明','小红','小刚']
#
# scores = {'小明':95,'小红':90,'小刚':90}
#
# print(len(students))
#
# print(len(scores))
# scores = {'小明':95,'小红':90,'小刚':90}
#
# print(scores['小明'])


# scores = {'小明':95,'小红':90,'小刚':90}
#
# scores['小刚']=92
#
# scores['小美']=85
#
# print(scores)

# students = {
# #     '第一组':['小明','小红','小刚','小美'],
# #     '第二组':['小强','小兰','小伟','小芳']
# #     }
# # print(students['第一组'][2])
# # #取出'第一组'对应列表偏移量为3的元素，即'小美'
# #
# # # 最外层是中括号，所以是列表嵌套字典，先判断字典是列表的第几个元素，再找出要取出的值相对应的键
# # scores = [
# #     {'小明':95,'小红':90,'小刚':100,'小美':85},
# #     {'小强':99,'小兰':89,'小伟':93,'小芳':88}
# #     ]
# # print(scores[0]['小刚'])


# dict = {'日本':'东京','英国':'伦敦','法国':'巴黎'}
#
# for i in dict:
#
#     print(i)


# man = ''  # 注：这个''代表空字符串
# while man != '有':
#     man = input('有没有愿意为小龙女死的男人？没有的话就不能出古墓。')
#
# print('小龙女可以出古墓门下山啦~')

# psw = ''
# while psw != '816':
#     psw = input('请输入密码： ')
# print('密码正确，已开门')

# stu = ['XM','XG','XH']
# for i in range(3):
#     stu1 = stu[0]
#     stu.append(stu1)
#     del stu[0]
#     print(stu)

#

# print(3<5)
#
# print(3>5)
#
# print('长安'=='长安')
#
# print('长安'!='金陵')



# for i in range(5):
#
#     print('明日复明日')
#
#     if i==3:  # 当i等于3的时候触发
#
#         continue # 回到循环开头
#
#     print('这句话在i等于3的时候打印不出来')

# a = 24
# while True:
#     b = int(input('请输入一个数字，我会告诉你是大了还是小了: '))
#     if b == 24:
#         print('嗯，答对了，恭喜\n')
#         break
#     if b < 24:
#         print('这个小了点~~\n')
#         continue
#     if b > 24:
#         print('这个大了点呢~~\n')
#         continue
#


#
# def tree(Height):
#
#     print('Merry Christmas!')
#
#     for i in range(Height):
#
#         print((Height-i)*2*' '+'o'+ i*'~x~o')
#
#         print(((Height-i)*2-1)*' '+(i*2+1)*'/'+'|'+(i*2+1)*'\\')
#
# tree(4)
#
# tree(8)
# def face(name):
#     return name + '的脸蛋'
# def body(name):
#     return name + '的身材'
# def main(like_face,like_body):
#     return '梦中情人的样子： '+face(like_face)+ '和' +body(like_body)
# print(main('AA','BB'))

# def bigger(a,b):
#     if a > b:
#         return a
#     elif a == b:
#         return '一样'
#     else:
#         return b
# print(bigger(8888,8888))


# 查看注释，运行代码。

# import random
#
# import time
#
# # 将抽奖程序封装成函数
#
# def choujiang(q,w,e):  # 定义一个抽奖函数，带有3个参数，也就是3位候选人
#
#     luckylist = [q,w,e]  # 定义一个中奖名单的列表
#
#     a = random.choice(luckylist)  # 在中奖名单里面随机选择
#
#     print('开奖倒计时',3)
#
#     time.sleep(1)
#
#     print('开奖倒计时',2)
#
#     time.sleep(1)
#
#     print('开奖倒计时',1)
#
#     time.sleep(1)
#
#     image = '''
#
#     /\_)o<
#
#     |      \\
#
#     | O . O|
#
#     \_____/
#
#     '''
#
#     print(image)
#
#     print('恭喜'+a+'中奖！')
#
# choujiang('虚竹','萧峰','段誉')  # 调用函数

# def cards():
#
#   color = ['红心', '方块', '梅花','黑桃']  # 将花色放在一个列表中待用
#
#   num = list(range(2, 11))
#
#   num.extend('JQKA')  # 通过两行代码，生成一个 2-A 的数字列表。
#
#   return [(x, y) for x in color for y in num ]  # 用列表生成式完成扑克牌的生成。
#
# print(cards())


import random
import time

player_win = 0
enemy_win = 0

while True:
  for i in range(1,4):

      player_life = random.randint(50, 100)
      player_attack = random.randint(50, 100)

      enemy_life = random.randint(50, 100)
      enemy_attack = random.randint(50, 100)

      print('这是第{}局'.format(i))
      time.sleep(1)
      print('【玩家】\n血量： {}\n攻击： {}'.format(player_life,player_attack))
      time.sleep(1)
      print('--------------------------------')
      time.sleep(1)
      print('【敌人】\n血量： {}\n攻击： {}'.format(enemy_life,enemy_attack))
      time.sleep(1)
      print('--------------------------------')

      while (player_life >= 0) and (enemy_life >= 0):
          player_life = player_life - enemy_attack
          enemy_life = enemy_life -player_attack
          print('敌人发起了攻击，玩家目前血量为 {}\n'.format(player_life))
          time.sleep(0.5)
          print('玩家发起了攻击，敌人的目前血量为 {}\n'.format(enemy_life))
          time.sleep(0.5)
          print('--------------------------------')
          time.sleep(1)


      if (player_life > 0) and (enemy_life <=0):
          print('玩家获胜\n')
          player_win = player_win +1
          time.sleep(1)
      elif (player_life <= 0) and (enemy_life >0):
          print('敌人赢了\n')
          enemy_win = enemy_win +1
          time.sleep(1)
      else:
          print('不好，同归于尽了\n')
          time.sleep(1)

  again = input('是否需要再来一局呢？ 请输入 (Y/N)  ')
  if again == 'Y':
      continue
  else:
      break

print('现在三局已经结束，公布最终结果： \n')
time.sleep(2)
print('最终结果就是。。。。。。。。。\n')
time.sleep(1.5)
print('玩家一共胜利了{}次\n'.format(player_win))
print('敌人一共胜利了{}次\n'.format(enemy_win))
if player_win > enemy_win:
    print('玩家赢了')
elif player_win < enemy_win:
    print('敌人赢了')
else:
    print('平局！')

