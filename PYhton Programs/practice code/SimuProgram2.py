"""
Do a program on pi determination considering the centre (0,0) where input of radius and number of simulation
should be taken as input by the user. Random number selection should be done during compilation.
Show the full calculation in the output.
"""

import random

radius = float(input("Enter radius : "))
x = 1000

point_1 = 0
point_2 = 0

for i in range(x ** 2):

    rand_x = random.uniform(-1, 1)
    rand_y = random.uniform(-1, 1)

    origin_dist = rand_x ** 2 + rand_y ** 2

    # Checking if (x, y) lies inside the circle
    if origin_dist <= 1:
        point_1 += 1

    point_2 += 1

    pi = 4 * point_1 / point_2

area = pi * radius * radius
print(f'Random Number is : {area}')
