#!/usr/bin/env python

from collections import namedtuple
from itertools import izip, islice

Code = namedtuple('PRN_generation_recipe', ('numbits', 'pop_taps', 'delay', 'first_n_chips_oct'))

CODES = {1: {'CA_G2i':Code(10, (2, 6),   5, '1440'), 'P':Code(12, ( 1,),  1, '4444')},
         2: {'CA_G2i':Code(10, (3, 7),   6, '1620'), 'P':Code(12, ( 2,),  2, '4000')},
         3: {'CA_G2i':Code(10, (4, 8),   7, '1710'), 'P':Code(12, ( 3,),  3, '4222')},
         4: {'CA_G2i':Code(10, (5, 9),   8, '1744'), 'P':Code(12, ( 4,),  4, '4333')},
         5: {'CA_G2i':Code(10, (1, 9),  17, '1133'), 'P':Code(12, ( 5,),  5, '4377')},
         6: {'CA_G2i':Code(10, (2,10),  18, '1455'), 'P':Code(12, ( 6,),  6, '4355')},
         7: {'CA_G2i':Code(10, (1, 8), 139, '1131'), 'P':Code(12, ( 7,),  7, '4344')},
         8: {'CA_G2i':Code(10, (2, 9), 140, '1454'), 'P':Code(12, ( 8,),  8, '4340')},
         9: {'CA_G2i':Code(10, (3,10), 141, '1626'), 'P':Code(12, ( 9,),  9, '4342')},
        10: {'CA_G2i':Code(10, (2, 3), 251, '1504'), 'P':Code(12, (10,), 10, '4343')},
        11: {'CA_G2i':Code(10, (3, 4), 252, '1642'), 'P':Code(12, (11,), 11, '4343')},
        12: {'CA_G2i':Code(10, (5, 6), 254, '1750'), 'P':Code(12, (12,), 12, '4343')},
        13: {'CA_G2i':Code(10, (6, 7), 255, '1764'), 'P':Code(12, (13,), 13, '4343')},
        14: {'CA_G2i':Code(10, (7, 8), 256, '1772'), 'P':Code(12, (14,), 14, '4343')},
        15: {'CA_G2i':Code(10, (8, 9), 257, '1775'), 'P':Code(12, (15,), 15, '4343')},
        16: {'CA_G2i':Code(10, (9,10), 258, '1776'), 'P':Code(12, (16,), 16, '4343')},
        17: {'CA_G2i':Code(10, (1, 4), 469, '1156'), 'P':Code(12, (17,), 17, '4343')},
        18: {'CA_G2i':Code(10, (2, 5), 470, '1467'), 'P':Code(12, (18,), 18, '4343')},
        19: {'CA_G2i':Code(10, (3, 6), 471, '1633'), 'P':Code(12, (19,), 19, '4343')},
        20: {'CA_G2i':Code(10, (4, 7), 472, '1715'), 'P':Code(12, (20,), 20, '4343')},
        21: {'CA_G2i':Code(10, (5, 8), 473, '1746'), 'P':Code(12, (21,), 21, '4343')},
        22: {'CA_G2i':Code(10, (6, 9), 474, '1763'), 'P':Code(12, (22,), 22, '4343')},
        23: {'CA_G2i':Code(10, (1, 3), 509, '1063'), 'P':Code(12, (23,), 23, '4343')},
        24: {'CA_G2i':Code(10, (4, 6), 512, '1706'), 'P':Code(12, (24,), 24, '4343')},
        25: {'CA_G2i':Code(10, (5, 7), 513, '1743'), 'P':Code(12, (25,), 25, '4343')},
        26: {'CA_G2i':Code(10, (6, 8), 514, '1761'), 'P':Code(12, (26,), 26, '4343')},
        27: {'CA_G2i':Code(10, (7, 9), 515, '1770'), 'P':Code(12, (27,), 27, '4343')},
        28: {'CA_G2i':Code(10, (8,10), 516, '1774'), 'P':Code(12, (28,), 28, '4343')},
        29: {'CA_G2i':Code(10, (1, 6), 859, '1127'), 'P':Code(12, (29,), 29, '4343')},
        30: {'CA_G2i':Code(10, (2, 7), 860, '1453'), 'P':Code(12, (30,), 30, '4343')},
        31: {'CA_G2i':Code(10, (3, 8), 861, '1625'), 'P':Code(12, (31,), 31, '4343')},
        32: {'CA_G2i':Code(10, (4, 9), 862, '1712'), 'P':Code(12, (32,), 32, '4343')},
        33: {'CA_G2i':Code(10, (5,10), 863, '1745'), 'P':Code(12, (33,), 33, '4343')},
        34: {'CA_G2i':Code(10, (4,10), 950, '1713'), 'P':Code(12, (34,), 34, '4343')},
        35: {'CA_G2i':Code(10, (1, 7), 947, '1134'), 'P':Code(12, (35,), 35, '4343')},
        36: {'CA_G2i':Code(10, (2, 8), 948, '1456'), 'P':Code(12, (36,), 36, '4343')},
        37: {'CA_G2i':Code(10, (4,10), 950, '1713'), 'P':Code(12, (37,), 37, '4343')}}

def taps_to_list(n, taps):
    return [(1 if t+1 in taps else 0) for t in range(n)]

def shift_register(state, feedback_taps, pop_taps):
    assert len(state) == len(pop_taps)
    while True:
        feedback  = sum(s*t for (s,t) in zip(state, feedback_taps)) % 2 
        pop_value = sum(s*t for (s,t) in zip(state, pop_taps)) % 2
        state = [feedback] + state[:-1]
        yield pop_value

def prn_ca(n):
    """Binary sequence modulating the Coarse Acquisition
    signal in GPS
    """
    recipe = CODES[n]['CA_G2i']
    G1 = shift_register(state=recipe.numbits*[1], 
                        feedback_taps=taps_to_list(recipe.numbits, (3,10)),
                        pop_taps=(recipe.numbits-1)*[0]+[1])
    G2 = shift_register(state=recipe.numbits*[1], 
                        feedback_taps=taps_to_list(recipe.numbits, (2,3,6,8,9,10)),
                        pop_taps=taps_to_list(recipe.numbits, recipe.pop_taps))
    for G1_pop, G2_pop in izip(G1, G2):
        yield G1_pop ^ G2_pop
