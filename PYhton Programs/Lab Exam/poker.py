import math

ObsFr = []
ExFr = []
ObsExFr = []
sum = 0
alpha = float(input("Enter the vlaue of Alpha: "))
Dalpha = float(input("Enter the vlaue of Dalpha: "))
print("Enter the value for Observed frequency: ")
for i in range(0, 7):
    val = int(input())
    ObsFr.append(val)

FiveDiffDigits = (10 / 10) * (9 / 10) * (8 / 10) * (7 / 10) * (6 / 10) * (math.factorial(5) / math.factorial(5))
FiveDiffDigits = round((FiveDiffDigits * 10000), 0)
ExFr.append(FiveDiffDigits)
Pairs = (10 / 10) * (1 / 10) * (9 / 10) * (8 / 10) * (7 / 10) * (
            math.factorial(5) / (math.factorial(2) * math.factorial(3)))
Pairs = round((Pairs * 10000), 0)
ExFr.append(Pairs)
TwoPairs = 0.5 * (10 / 10) * (1 / 10) * (1 / 10) * (9 / 10) * (8 / 10) * (
            math.factorial(5) / (math.factorial(2) * math.factorial(2) * math.factorial(1)))
TwoPairs = round((TwoPairs * 10000), 0)
ExFr.append(TwoPairs)
ThreeofKind = (10 / 10) * (1 / 10) * (1 / 10) * (9 / 10) * (8 / 10) * (
            math.factorial(5) / (math.factorial(3) * math.factorial(2)))
ThreeofKind = round((ThreeofKind * 10000), 0)
ExFr.append(ThreeofKind)
FullHouse = (10 / 10) * (1 / 10) * (1 / 10) * (9 / 10) * (1 / 10) * (
            math.factorial(5) / (math.factorial(3) * math.factorial(2)))
FullHouse = round((FullHouse * 10000), 0)
ExFr.append(FullHouse)
FourofKind = (10 / 10) * (1 / 10) * (1 / 10) * (1 / 10) * (9 / 10) * (
            math.factorial(5) / (math.factorial(4) * math.factorial(1)))
FourofKind = round((FourofKind * 10000), 0)
ExFr.append(FourofKind)
FiveofKind = (10 / 10) * (1 / 10) * (1 / 10) * (1 / 10) * (1 / 10) * (
            math.factorial(5) / (math.factorial(5) * math.factorial(0)))
FiveofKind = round((FiveofKind * 10000), 0)
ExFr.append(FiveofKind)

for i in range(0, 7):
    calculatedVal = ((ObsFr[i] - ExFr[i]) * (ObsFr[i] - ExFr[i])) / ExFr[i]  # (obsfr - exfr) * (obsfr - exfr)/exfr
    calculatedVal = round(calculatedVal, 4)
    ObsExFr.append(calculatedVal)
    sum += calculatedVal  # total calculatedVal

print("The value of Observed Frequency:  ", ObsFr)
print("The value of Expected Frequency:  ", ExFr)
print("The value of calculation of Observed and Expected Frequency:  ", ObsExFr)
print("The value of X0: ", sum)

if Dalpha > sum:
    ind = (1 - alpha) * 100
    print("*Since the computed value", sum, "is less than Dalpha* \n The random numbers are independent at: ", ind, "%")

else:
    print("The random numbers are not independent")
