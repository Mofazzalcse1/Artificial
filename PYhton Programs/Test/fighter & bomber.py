import math

s = 20
xb = 100  # , 110, 120, 129, 140, 149, 158, 168, 179, 188, 198, 209, 219, 226, 234, 240
yb = 0  # , 3, 6, 10, 15, 20, 26, 32, 37, 34, 30, 27, 23, 19, 16, 14
xf = 0
yf = 60

dist = math.sqrt((yb - yf ** 2) + (xb - xf) ** 2)

sin = (xb - yf) / dist
cos = (xb - xf) / dist

xf_new = xf + s * cos
# xf.append(xf_new)
yf_new = yf + s * sin
# yf.append(yf_new)
print(dist)
print(sin)
print(cos)