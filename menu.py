"""
MENU CONTROL
"""

# date 2023 03 29 17:45
# location 35 33

import sys
import time
import fake

now = time.time()
now = int(now)

def user_prompt():
    """ 
    User user_prompt 
    """
    askuser = input("$ ")
    askuser = str(askuser.lower())
    #print(askuser)
    if askuser == 'l':
        print(askuser)
        print(now)
        fake.fake_lcg(now,1145,1140,1680)
        user_prompt()
    if askuser == 'x':
        print(askuser)
        fake.xor_shift(113140)
        user_prompt()
    if askuser == 'y':
        print(askuser)
        fake.laby()
        user_prompt()
    if askuser == 'q':
        print(askuser)
        sys.exit()
    if askuser == '':
        print(askuser)
        user_prompt()
    if askuser != '':
        print(askuser)
        user_prompt()
    if askuser == 'h':
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
    print("Y. LAB Y")
    print("Q. QUIT")
    print("H. HELP LIST")

    user_prompt()
