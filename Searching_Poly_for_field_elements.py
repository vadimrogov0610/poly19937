"""
A -- any element in GF(2^19937)
code finds all the powers of A:
A^0, ..., A^19937
this set is linearly dependent, therefore there is an polynomial
A^0 + ... + A^19937 = 0
the code returns this polynomial for every A
"""
from typing import Dict
from time import process_time
from random import randint as ri
from Poly19937 import Poly19937


D = {}
Ind = {}

A = Poly19937(ri(1, (1 << 19937) - 1))  # any element of the field
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
