"""
MENU CONTROL
"""

# date 2023 03 29 17:45
# location 35 33

import sys
import fake


def user_prompt():
    """ 
    User user_prompt 
    """
    askuser = input("$ ")
    askuser = str(askuser.upper())
    #print(askuser)
    if askuser == 'L':
        print(askuser)
        fake.fake_lcg(1041,1145,1140,1680)
        user_prompt()
    if askuser == 'X':
        print(askuser)
        fake.xor_shift(113140)
        user_prompt()
    if askuser == 'Q':
        print(askuser)
        sys.exit()
    if askuser == '':
        print(askuser)
        user_prompt()
    if askuser != '':
        print(askuser)
        user_prompt()
    if askuser == 'H':
        print(askuser)
        menu_card()
        user_prompt()

def menu_card():
    """ 
    Give some help to the user
    """
    print("-- MAIN MENU --")
    print("L. fake lcg")
    print("X. XOR SHIFT")
    print("Q. QUIT")
    print("H. HELP LIST")
    user_prompt()
