import random

n = int(input("Enter the number of random numbers: "))
start = float(input("Enter the value of Start range of Random number : "))
end = float(input("Enter the value of End range of Random number : "))
alpha = float(input("Enter the value of alpha: "))
alpha = round(alpha, 2)
Dalpha = float(input("Enter the value of D alpha: "))
Dalpha = round(Dalpha, 3)


def Rand(start, end, n):
    li = []

    for j in range(n):
        li.append(random.uniform(start, end))

    return li


R = Rand(start, end, n)

R.sort()
Dp = []
Dm = []
A = []

# i/n --- A=[]
for i in range(0, n):
    a = (i + 1) / n
    A.append(a)

    A[i] = round(A[i], 2)
    if a > R[i]:  # i/n > Ri
        Dp.append(round(a - R[i], 2))  # i/n - Ri
    else:
        Dp.append(0)

    if i == 0:
        Dm.append(R[i])
        continue
    else:
        if i == 1:
            b = i / n
        else:
            b = (i - 1) / n
        if R[i] > b:
            Dm.append(round(R[i] - b, 2))  # Ri - (i-1)/n
        else:
            Dm.append(0)

DpMax = max(Dp)
DmMax = max(Dm)

D = max(DpMax, DmMax)

print("Alpha = ", alpha)
print("Dalpha = ", Dalpha)
print("Given Random numbers are: ", R)
print("i/N is:  ", A)
print("D+ = ", Dp, "\n and maximum of D+ is ", DpMax)
print("D- = ", Dm, "\n and maximum of D- is ", DmMax)
print("Largest Deviation D = ", D)

if D < Dalpha:
    CL = int(round(1 - alpha, 2) * 100)
    print(
        f"*(Since the computed value {D} is less than Dalpha)* \n Given random numbers are uniform at {CL}% confidence level. ")
else:
    print("Given random numbers are not uniform")