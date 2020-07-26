print('接下来请输入两个数字，我会把他们相除\n')
print("如果不想玩儿了，就输入 ‘离开’ 两个字就可以滚蛋了\n")

while True:
    fn = input('那么请输入第一个数字： ')
    if fn == '离开':
        break
    print('\n')
    sn = input('然后请输入第二个数字： ')
    if sn == '离开':
        break
    print('\n')
    try:
        ansewer = int(fn) / int(sn)
    except ZeroDivisionError:
        print('不要调皮哦，0又不能作为除数~~\n')
    except ValueError:
        print('不要瞎搞啊喂\n')
    else:
        print(ansewer)
