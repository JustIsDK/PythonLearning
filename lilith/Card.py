import collections
from random import choice
Card = collections.namedtuple('Card',['rank','suit'])

'''
生成扑克牌的代码
先生成一个数组
下面的函数往这个数组中填充
看不懂
'''

class FreachDeck:
    ranks = [str(n) for n in range(2,11)]+ list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank,suit) for suit in self.suits
                      for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]

deck = FreachDeck()

suit_value = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FreachDeck.ranks.index(card.rank)
    return rank_value * len(suit_value) + suit_value[card.suit]

for card in sorted(deck,key=spades_high):
    print(card)
