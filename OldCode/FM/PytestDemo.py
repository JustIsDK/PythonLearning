def test_pass():
     assert (1,2,3) == (1,2,3)

'''此处为被测方法,在PytestDemo1被引用'''
'''这个方法是个选出set中最大值的方法'''
def max(value):
    _max = value[0]
    for val in value:
        if val > _max:
            _max = val
    return _max

def min(values):

  _min = values[0]
  for val in values:
      if val < _min:
          _min = val

  return _min