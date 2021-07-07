import pytest

import PytestDemo
'''这个是引入另一个文件中的方法，那个文件中的是被测方法'''

def test_max():
    '''这里写的是测试用被测方法的方法'''
    value = (2,1,3,5,2,7)
    '''这里赋值给待测方法'''
    val = PytestDemo.max(value)
    '''把被测方法的值赋值给val'''
    assert val == 7
    '''做断言'''
@pytest.mark.skip
def test_min():
    values = (2, 3, 1, 4, 6)

    val = PytestDemo.min(values)
    assert val == 1