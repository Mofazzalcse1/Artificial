import random
import math


def random_walk(n):
    x = 0
    y = 0
    for i in range(n):
        step = random.choice(['N', 'S', 'E', 'W'])
        if step == 'N':
            y = y + 1
        elif step == 'S':
            y = y - 1
        elif step == 'E':
            x = x + 1
        else:
            x = x - 1
    return x, y


x = int(input("Enter Number of Step: "))

for i in range(x):
    walk = random_walk(10)
    print(walk, "Distance from Every Step = ", abs(walk[0]) + abs(walk[1]))
