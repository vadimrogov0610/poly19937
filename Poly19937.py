"""
class Poly19937 -- числа от 0 до 2^19937 - 1
отвечающие c0 + c1a + c2a^2 + ... + c19936a^19936 in GF(2^19937)
реализованы арифметические операции. reduce -- сведение по модулю f ( = cp)
"""
from time import process_time


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

    def __eq__(self, other):
        return self.i == other.i

    def __copy__(self):
        return Poly19937(self.i)

    def reduce(self):  # mod f
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

    def __pow__(self, power):  # не работает почему-то
        if power == 0:
            return Poly19937(1)
        if power == 2:
            y = self.i
            ans = 0
            while y:
                bl = y.bit_length() - 1
                ans ^= 1 << (2*bl)
                y ^= 1 << bl
            Ans = Poly19937(ans)
            Ans.reduce()
            return Ans
        if power & 1:
            return self * pow(self, power - 1)
        return pow(pow(self, 2), power // 2)


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
f = sum(1 << i for i in cp)  # characteristic poly

# EXAMPLE:
"""B = Poly19937(1 << 50000)

N = 65537

print(f'B = {B}')
B.reduce()
ttt = process_time()
print(f'POW(B, {N}) = {pow(B, N)}')
print(f'pow time = {process_time() - ttt}')

ttt = process_time()
S = Poly19937(1)
for i in range(N):
    S *= B
print(f'B^{N} = {S}')
print(f'usual time: = {process_time() - ttt}')

print(S.i == pow(B, N).i)"""
