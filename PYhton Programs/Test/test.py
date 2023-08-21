with open("1.txt") as file:
    content = file.readlines()
    N = [i.strip() for i in content]

RandomNumber = []

for x in N:
    RandomNumber.append(int(x))

print(RandomNumber)
