"""
kino-random/fake.py
library for random algorithms
"""
#date 2023 03 29 13:40
#location 35 33
#authpr renosgps
#
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
