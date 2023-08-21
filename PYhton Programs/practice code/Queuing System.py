mean = float(input("Enter mean value :"))
SD = float(input("Enter SD :"))

rand = [-0.46, -1.15, 0.15, 0.81, 0.74, -0.39, 0.45, 2.44, 0.59, -0.06, 0.09, 0.56, 0.65, 3.10, -0.44]
for x in range(1, 16):
    print(x)
print(".......................")
for r in rand:
    print(r)

print("......................")

for i in rand:
    IAT = mean + SD * i
    print(IAT)
print("..................")

x = 0
for i in range(0, len(rand)):
    x += (mean + SD * rand[i])
    print(x)
print("-----------------------------")

N_random = [0.59, -0.67, 0.41, 0.51, 1.53, -0.37, -0.27, - 0.15, -0.02, -1.60, -0.19, -0.16, -0.07, 0.24, -1.76]
for x1 in N_random:
    print(x1)

mean2 = float(input("Enter mean2 value :"))
SD2 = float(input("Enter SD :"))

for x2 in N_random:
    x = mean2 + SD2 * x2
    print(x)
print("......................")

cum = mean + SD * (rand[0])
servEnd = mean2 + SD2 * (N_random[0])
x = 0
total = cum + servEnd
print(total)
print("................")
x = (mean + SD * rand[0])
print(x)
for i in range(1, len(rand)):
    total += (mean + SD2 * (N_random[i - 1]))

    x += (mean + SD * rand[i])

    if x > total:
        print(x)


    else:
        print(total)

cum = mean + SD * (rand[0])

total = cum + servEnd

for i in range(1, 15):
    total += (mean2 + SD2 * (N_random[i]))
    print(total)
print(f"Spend : {total}")

cum = mean + SD * (rand[0])
servEnd = mean2 + SD2 * (N_random[0])
x = 0
total = cum + servEnd
x = (mean + SD * rand[0])
print(abs(x - total))
for i in range(1, len(rand)):
    total += (mean + SD2 * (N_random[i - 1]))
    x += (mean + SD * rand[i])
    waitingTime = abs(total - x)
    print(waitingTime)
