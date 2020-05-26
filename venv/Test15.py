# def get_full_name(first,last):
#     full_name = first + ' ' + last
#     return full_name.title()

# The_name = get_full_name('D','K')
# print(The_name)

# from Test14 import get_full_name
# print("Enter 'q' at any time to quit")
# while True:
#     first = input('\nPlease enter your first name: ')
#     if first == 'q':
#         break
#     last = input('\nPlease enter your last name: ')
#     if last == 'q':
#         break
#
#     format_name = get_full_name(first, last)
#     print('\nYour format name is: ' + format_name + ' ~~')

import unittest
from Test14 import get_full_name

class NameTestCase(unittest.TestCase):

    # def test_first_name(self):
    #     full_name = get_full_name('d','k')
    #     self.assertEqual(full_name,'D K')

    def test_middle_name(self):
        full_name = get_full_name('d','c','n')
        self.assertEqual(full_name,'D C N')

unittest.main()