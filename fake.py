"""
kino-random/fake.py
library for random algorithms
"""
#date 2023 03 29 13:40
#location 35 33
#authpr renosgps
#
import random
# [LCG]--------------------------------------------------
def fake_lcg(x_seed,a_mult,c_inc,m_modulo):
    """ 
    DOCSTRING fake Linear Congrucated Generator
    Seed = Seed * Multi + increment % modulo
    x: seed
    a: Multiplier
    c: Increment
    m: modulo
    """
    x_seed = x_seed * a_mult + c_inc % m_modulo
    print(f"LCG : {x_seed}")
# [xor-shift]----------------------------------------------
def xor_shift(x_seed):
    """ 
    XOR SHIFT

    """

    x_seed ^= x_seed << 13
    x_seed ^= x_seed >> 7
    x_seed ^= x_seed << 17
    print (f"XOR SHIFT: {x_seed}")

# [lab Y]----------------------------------------------
def laby():
    """
    DOCSTR
    """
    unix_limit= 2147483647
    unixts = 0
    gendraw = ()
    drawone = (2,5,7,8,22,33,38,44,46,52,54,55,56,58,62,63,66,72,74,78)
    print(drawone)
    for _ in range(1,201):
        random.seed(unixts)
        unixts = unixts + 1
        gendraw = random.sample(80,20)
        sorted(gendraw)
        print(unixts)
        print(random.seed())
        print(drawone)
        print(gendraw)
        #if (gendraw == drawone):
        #    print(drawone)
        #    break
