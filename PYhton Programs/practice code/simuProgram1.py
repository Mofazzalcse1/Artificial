"""
1. Do a program on unbiased coin problem where user should be able to take number of games to be played,
 how much money to pay, difference value, how much money shall he get.You sent Random number assignment for
the coins and random number selection in each game should be done during compilation (NO MANUAL ENTRY)
"""

import random

try:
    coin = ['H', 'T']
    gameNo = int(input("Enter Number of Game you want to play: "))
    payPerChance = float(input("How much Money You want to spend per chance : "))
    win = 0
    lost = 0
    for i in range(1, gameNo + 1):
        x = input("Enter Your Chose : For Head 'H' or For Tail 'T'")
        if x == random.choice(coin):
            print("You are win . ")
            win = win + 1
        else:
            print("You are lost .")
            lost = lost + 1

    spend_money = gameNo * payPerChance
    print(f"You are win {win} times and lost {lost} times .")
    print(f"You spend {spend_money} dollar .")

except:
    print("You Entered Wrong Value.Please Enter Right Value .")
