# # # # # i = 1
# # # # # while i <= 100:
# # # # #     print(i)
# # # # #     i = i + 2
# # # # # print("program END")
# # # # #
# # # #
# # # # i: int = 1
# # # # while i <= 100:
# # # #     print(i, "bangladesh")
# # # #     i += 1
# # # # print("End")
# # #
# # # num = int(input("enter any number :"))
# # # Sum = 0
# # #
# # # for x in range(1, num + 1, 1):
# # #     Sum = Sum + x**2
# # #
# # # print(Sum)
# #
# # num = int(input("Enter the number: "))
# #
# # for x in range(num + 1):
# #     print(x * " * ")
#
# rows = 6
# for num in range(rows):
#     for i in range(num):
#         print (num,end="")
#     print(" ")

num = 5
for i in range(num):
    for j in range(1, num - 1):
        print(" ", end="")
    for k in range(0, i + 1):
        print(" *", end="")
    print(" ")
