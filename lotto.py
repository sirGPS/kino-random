"""
Lotto equations


"""
# date 2023 04 05 #12:00
# Location 35 33
# author RenosGPS



# KINO
# 80 / 20 / 12..1

def kino_pool():
    pool = []
    for index in range(1,81):
        pool.append(index)
    print(pool)

def lotto_pool():
    pool = []
    for index in range(1,61):
        pool.append(index)
    print(pool)

def joker_pool():
    pool = []
    for index in range(1,45):
        pool.append(index)
    print(pool)