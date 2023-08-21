TimeBetweenArrival = 8

print("Time Between Arrival ")
for i in range(1, TimeBetweenArrival + 1):
    print(i)

print("Probability : ")
rand = 1 / TimeBetweenArrival

for x in range(1, TimeBetweenArrival + 1):
    print(rand)

cum = 0
print("cumulative Probability: ")
for z in range(1, TimeBetweenArrival + 1):
    cum += rand
    print(cum)

print("Random Number Assignment :")
for v in range(0, 1001, 125):
    if v == 0:
        print("001 - 125")
    elif v == 125:
        print("126 - 250")
    elif v == 250:
        print("251 - 375")
    elif v == 375:
        print("376- 500")
    elif v == 500:
        print("501 - 625")

    elif v == 625:
        print("626 - 750 ")
    elif v == 750:
        print("751- 875")
    elif v == 875:
        print("876 - 000")

print("Customer : ")
for a in range(21):
    print(a)

RandomNumber = [913, 727, 15, 948, 309, 922, 753, 235, 302, 109, 93, 607, 738, 359, 888, 106, 212, 493, 535]
RandomNumber2 = [84, 10, 74, 53, 17, 79, 91, 67, 89, 38, 32, 94, 79, 5, 79, 84, 52, 55, 30, 50]
print("Random Number : ")
for N in RandomNumber:
    print(N)
TM = []
print("Time between Arrival : ")
for x in RandomNumber:
    if 0 <= x < 125:
        TM.append(1)
    elif 126 <= x <= 250:
        TM.append(2)
    elif 251 <= x <= 375:
        TM.append(3)
    elif 376 <= x <= 500:
        TM.append(4)

    elif 501 <= x <= 625:
        TM.append(5)
    elif 626 <= x <= 750:
        TM.append(6)
    elif 751 <= x <= 875:
        TM.append(7)
    elif 876 <= x < 1000:
        TM.append(8)
print(TM)

print("Service Time : ")
for server in range(1, 7):
    print(server)

print("Probability : ")
rand2 = [0.10, 0.20, 0.30, 0.25, 0.10, 0.05]
for r in rand2:
    print(r)

CAT = []
print("Cumulative Probability: ")
x1 = 0
for j in rand2:
    x1 += j
    CAT.append(x1)
print(CAT)

print("Random Number Assignment : ")
for j in range(1, 101, 18):
    if j == 1:
        print("01 - 10")
    elif j == 19:
        print("11 - 30")

    elif j == 37:
        print("31 - 60")

    elif j == 55:
        print("61 - 85")
    elif j == 73:
        print("86 - 95")
    else:
        print("96 - 00")

print("\nTotal Customer : \n")
for x1 in range(1, 21):
    print(x1, end=" ")

print("\nRandom Number : \n")
for rn in RandomNumber2:
    print(rn, end=" ")

print("\nTime Arrival Time : \n")
for x3 in TM:
    print(x3, end=" ")

print("\n Cumulative Arrival Time \n")
cs = 0
CAT1 = [0]
for ct in TM:
    cs += ct
    CAT1.append(cs)

for xt in CAT1:
    print(xt, end=" ")

print("\n\nService Time ST : \n")
st = []
for sr in RandomNumber2:
    if 1 <= sr <= 10:
        st.append(1)
    elif 11 <= sr <= 30:
        st.append(2)

    elif 31 <= sr <= 60:
        st.append(3)

    elif 61 <= sr <= 85:
        st.append(4)
    elif 86 <= sr <= 95:
        st.append(5)
    else:
        st.append(6)
print(st)

print("Time Service Began : ")
SB = [0]
SE = SB[0] + st[0]
print(SE)
