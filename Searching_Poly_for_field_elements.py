"""
A = a^n в поле GF(2^19937)
находит все степени A до 19937:
A^0, ..., A^19937
эта совокупность линейно зависима, возвращает полином
A^0 + ... + A^19937 = 0
"""
from typing import Dict
from time import process_time
from random import randint as ri


class Poly19937:
    def __init__(self, i: int):
        self.i = i

    def __bool__(self):
        return bool(self.i)

    def __repr__(self):
        y = self.i
        if not y:
            return '0'
        lst = []
        while y:
            bl = y.bit_length() - 1
            lst.append(f'a^{bl}')
            y ^= 1 << bl
        return ' + '.join(reversed(lst))

    def reduce(self):
        bl = self.i.bit_length() - 1
        while bl >= 19937:
            self.i ^= f << (bl - 19937)
            bl = self.i.bit_length() - 1

    def __add__(self, other):
        return Poly19937(self.i ^ other.i)

    def __mul__(self, other):
        y = other.i
        ans = 0
        while y:
            bl = y.bit_length() - 1
            ans ^= self.i << bl
            y ^= 1 << bl
        Ans = Poly19937(ans)
        Ans.reduce()
        return Ans


def add_basic(d: Dict[int, int], elem: int, ind: Dict[int, int], row: int):
    num = elem.bit_length()
    ans = 1 << row
    while num in d:
        elem ^= d[num]
        ans ^= ind[num]
        num = elem.bit_length()
    if num == 0:
        return False, ans
    d[num] = elem
    ind[num] = ans
    return True, None


cp = [
    0, 1189, 1416, 1585, 1643, 1870, 2493, 2773, 3000, 3227, 3454, 3681, 3908, 4135, 4362, 4753, 5661, 6337, 6569,
    7129, 7477, 7525, 7583, 7752, 7979, 8206, 9505, 9901, 9969, 10128, 10693, 10761, 10920, 11089, 11147, 11157,
    11215, 11321, 11374, 11384, 11485, 11611, 11712, 11717, 11838, 11881, 11944, 11997, 12277, 12335, 12393, 12504,
    12509, 12620, 12673, 12731, 12736, 12789, 12905, 12958, 12963, 13137, 13185, 13190, 13243, 13301, 13412, 13528,
    13533, 13639, 13697, 13760, 13813, 13866, 14093, 14151, 14209, 14320, 14325, 14436, 14547, 14552, 14605, 14721,
    14774, 14779, 14953, 15001, 15006, 15059, 15117, 15228, 15344, 15349, 15455, 15513, 15576, 15629, 15682, 15909,
    15967, 16025, 16136, 16141, 16252, 16363, 16368, 16421, 16537, 16590, 16595, 16817, 16822, 16875, 16933, 17044,
    17160, 17271, 17329, 17445, 17498, 17725, 17783, 17841, 17952, 18068, 18179, 18237, 18406, 18633, 18691, 18860,
    19087, 19314, 19937
]
f = sum(1 << i for i in cp)

D = {}
Ind = {}

A = Poly19937(ri(1, (1 << 5) - 1))
A.reduce()
print(f'A = {A}\nPoly:')

ttt = process_time()

S = Poly19937(1)
for i in range(19938):
    b, ind_set = add_basic(D, S.i, Ind, i)
    if not b:
        print(Poly19937(ind_set).__repr__().replace('a', 'A'))
        print(f'len = {bin(ind_set).count("1")}')
    S *= A
print(f'time: {process_time() - ttt}')
