#!/usr/bin/env python

from collections import namedtuple
from itertools import izip

Code = namedtuple('PRN_generation_recipe', ('numbits', 'taps', 'delay', 'n', 'first_n_chips_oct'))

CODES = {1: {'CA_G2i':Code(10, (2, 6),   5, 10, '1440'), 'P':Code(12, ( 1,),  1, 12, '4444')},
         2: {'CA_G2i':Code(10, (3, 7),   6, 10, '1620'), 'P':Code(12, ( 2,),  2, 12, '4000')},
         3: {'CA_G2i':Code(10, (4, 8),   7, 10, '1710'), 'P':Code(12, ( 3,),  3, 12, '4222')},
         4: {'CA_G2i':Code(10, (5, 9),   8, 10, '1744'), 'P':Code(12, ( 4,),  4, 12, '4333')},
         5: {'CA_G2i':Code(10, (1, 9),  17, 10, '1133'), 'P':Code(12, ( 5,),  5, 12, '4377')},
         6: {'CA_G2i':Code(10, (2,10),  18, 10, '1455'), 'P':Code(12, ( 6,),  6, 12, '4355')},
         7: {'CA_G2i':Code(10, (1, 8), 139, 10, '1131'), 'P':Code(12, ( 7,),  7, 12, '4344')},
         8: {'CA_G2i':Code(10, (2, 9), 140, 10, '1454'), 'P':Code(12, ( 8,),  8, 12, '4340')},
         9: {'CA_G2i':Code(10, (3,10), 141, 10, '1626'), 'P':Code(12, ( 9,),  9, 12, '4342')},
        10: {'CA_G2i':Code(10, (2, 3), 251, 10, '1504'), 'P':Code(12, (10,), 10, 12, '4343')},
        11: {'CA_G2i':Code(10, (3, 4), 252, 10, '1642'), 'P':Code(12, (11,), 11, 12, '4343')},
        12: {'CA_G2i':Code(10, (5, 6), 254, 10, '1750'), 'P':Code(12, (12,), 12, 12, '4343')},
        13: {'CA_G2i':Code(10, (6, 7), 255, 10, '1764'), 'P':Code(12, (13,), 13, 12, '4343')},
        14: {'CA_G2i':Code(10, (7, 8), 256, 10, '1772'), 'P':Code(12, (14,), 14, 12, '4343')},
        15: {'CA_G2i':Code(10, (8, 9), 257, 10, '1775'), 'P':Code(12, (15,), 15, 12, '4343')},
        16: {'CA_G2i':Code(10, (9,10), 258, 10, '1776'), 'P':Code(12, (16,), 16, 12, '4343')},
        17: {'CA_G2i':Code(10, (1, 4), 469, 10, '1156'), 'P':Code(12, (17,), 17, 12, '4343')},
        18: {'CA_G2i':Code(10, (2, 5), 470, 10, '1467'), 'P':Code(12, (18,), 18, 12, '4343')},
        19: {'CA_G2i':Code(10, (3, 6), 471, 10, '1633'), 'P':Code(12, (19,), 19, 12, '4343')},
        20: {'CA_G2i':Code(10, (4, 7), 472, 10, '1715'), 'P':Code(12, (20,), 20, 12, '4343')},
        21: {'CA_G2i':Code(10, (5, 8), 473, 10, '1746'), 'P':Code(12, (21,), 21, 12, '4343')},
        22: {'CA_G2i':Code(10, (6, 9), 474, 10, '1763'), 'P':Code(12, (22,), 22, 12, '4343')},
        23: {'CA_G2i':Code(10, (1, 3), 509, 10, '1063'), 'P':Code(12, (23,), 23, 12, '4343')},
        24: {'CA_G2i':Code(10, (4, 6), 512, 10, '1706'), 'P':Code(12, (24,), 24, 12, '4343')},
        25: {'CA_G2i':Code(10, (5, 7), 513, 10, '1743'), 'P':Code(12, (25,), 25, 12, '4343')},
        26: {'CA_G2i':Code(10, (6, 8), 514, 10, '1761'), 'P':Code(12, (26,), 26, 12, '4343')},
        27: {'CA_G2i':Code(10, (7, 9), 515, 10, '1770'), 'P':Code(12, (27,), 27, 12, '4343')},
        28: {'CA_G2i':Code(10, (8,10), 516, 10, '1774'), 'P':Code(12, (28,), 28, 12, '4343')},
        29: {'CA_G2i':Code(10, (1, 6), 859, 10, '1127'), 'P':Code(12, (29,), 29, 12, '4343')},
        30: {'CA_G2i':Code(10, (2, 7), 860, 10, '1453'), 'P':Code(12, (30,), 30, 12, '4343')},
        31: {'CA_G2i':Code(10, (3, 8), 861, 10, '1625'), 'P':Code(12, (31,), 31, 12, '4343')},
        32: {'CA_G2i':Code(10, (4, 9), 862, 10, '1712'), 'P':Code(12, (32,), 32, 12, '4343')},
        33: {'CA_G2i':Code(10, (5,10), 863, 10, '1745'), 'P':Code(12, (33,), 33, 12, '4343')},
        34: {'CA_G2i':Code(10, (4,10), 950, 10, '1713'), 'P':Code(12, (34,), 34, 12, '4343')},
        35: {'CA_G2i':Code(10, (1, 7), 947, 10, '1134'), 'P':Code(12, (35,), 35, 12, '4343')},
        36: {'CA_G2i':Code(10, (2, 8), 948, 10, '1456'), 'P':Code(12, (36,), 36, 12, '4343')},
        37: {'CA_G2i':Code(10, (4,10), 950, 10, '1713'), 'P':Code(12, (37,), 37, 12, '4343')}}

def bitLenCount(int_type):
    """total number of bits and number of set (1) bits in a binary representatino of int_type"""
    length = 0
    count = 0
    while (int_type):
        count += (int_type & 1)
        length += 1
        int_type >>= 1
    return(length, count)

def lfsr(nbits, state, feedback_taps, pop_taps=(10,), delay=0, stop_state=None):
    pop_bitmask = sum((1<<(nbits - t))  for t in pop_taps)
    while True:
        push_bit = 0
        for t in feedback_taps:
            push_bit ^= ((state & (1<<(nbits - t))) != 0)

        pop_bit = bitLenCount(state & pop_bitmask)[1] % 2   # %2 <=> &1

        state = (push_bit << nbits-1) + (state >> 1)
        if delay > 0:
            delay -= 1
        else:
            yield pop_bit, push_bit, state
        if stop_state and state == stop_state:
            break    

CA_nbits = 10

#for (G1_pop, _, _), (G2_pop, _, _) in izip(lfsr(CA_nbits, 0b1111111111, (3,10)),
#                                           lfsr(CA_nbits, 0b1111111111, (2,3,6,8,9,10), pop_taps=(10,), delay=1023-5)):
#    print G1_pop ^ G2_pop,

for (G1_pop, _, _), (G2_pop, _, _) in izip(lfsr(CA_nbits, 0b1111111111, (3,10)),
                                           lfsr(CA_nbits, 0b1111111111, (2,3,6,8,9,10), pop_taps=(2, 6), delay=0)):
    print G1_pop ^ G2_pop,

#for pop_bit, push_bit, state in lfsr(CA_nbits, 0b1111111111, (2,3,6,8,9,10)):
#    print pop_bit, push_bit, bin(2**CA_nbits+state)[3:]

