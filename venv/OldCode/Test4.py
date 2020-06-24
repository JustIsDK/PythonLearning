'''
needs=str(input('Please tell me what you want: '))
cars=['audi','auto','benz','ford']
if needs.lower() in cars:
    print('Let me see if I can find you a '+needs)
else:
    print('Sorry,we can not help you~')

num = int(input('Please tel me how mmany people come to res: '))
if num > 8:
    print('We have not enough seats fou you')
else:
    print('We have enough seats fou you,welcome! ')

num = int(input('Please input a number: '))
if num % 10 == 0:
    print('Yes!')
else:
    print('No')
'''
