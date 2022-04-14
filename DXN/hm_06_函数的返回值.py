def sum_2_sum(num1,num2):
    '''对两个数字的求和'''
    result=num1+num2
    '''可以使用返回值,告诉调用函数一方计算的结果'''
    return result
    '''return代表返回,后面的代码不会被执行'''

sum_result=sum_2_sum(10,20)
print('计算结果:%d'%sum_result)