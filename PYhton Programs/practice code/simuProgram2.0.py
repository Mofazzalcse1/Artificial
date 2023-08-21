"""
Do a program on pi determination considering the centre (0,0) where input of radius and number of simulation
should be taken as input by the user. Random number selection should be done during compilation.
Show the full calculation in the output.
"""

import random

radius = int(input("Enter radius : "))

simuNumber = int(input("Enter simulation number :"))


point_1 = 0
point_2 = 0


for i in range(1, simuNumber + 1):
    r1 = float(input("Enter r1 in range of zero to one:"))
    r2 = float(input("Enter r2 in range of zero to one :"))
    origin_dist = r1 ** 2 + r2 ** 2

    if origin_dist <= 1:
        point_1 += 1
    else:

        point_2 += 1

pi = 4 * point_1 / point_2
print("pi =", pi)

area = pi * radius * radius
print(f'Area is : {area}')
