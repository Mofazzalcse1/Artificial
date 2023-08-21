# def daily_demand(mean, sd, probability):
#     pass
#
#
# def monte_carlo_ray(M, product, review_period=30, day_demand=None):
#     inventory = product.starting_stock
#     mean = product.mean
#     sd = product.sd
#     lead_time = product.lead_time
#     probability = product.probability
#     demand_lead = product.demand_lead
#
#     q = 0
#     stock_out = 0
#     counter = 0
#     order_placed = False
#     # dictionary to store all the information
#     data = {'inv_level': [], 'daily_demand': [], 'units_sold': [], 'units_lost': [], 'orders': []}
#
#     for day in range(1, 365):
#         daily_demand(mean, sd, probability)
#         data['daily_demand'].append(day_demand)
#
#         if day % review_period == 0:
#             # Placing the order
#             q = M - inventory + demand_lead
#             order_placed = True
#             data['orders'].append(q)
#
#         if order_placed:
#             counter += 1
#
#         if counter == lead_time:
#             # Restocking day
#             inventory += q
#             order_placed = False
#             counter = 0
#
#         if inventory - day_demand >= 0:
#             data['units_sold'].append(day_demand)
#             inventory -= day_demand
#         elif inventory - day_demand < 0:
#             data['units_sold'].append(inventory)
#             data['units_lost'].append(day_demand - inventory)
#             inventory = 0
#             stock_out += 1
#
#         data['inv_level'].append(inventory)
#
#     return data

mean = 10
SD = 1.5

rand = [-0.46, -1.15, 0.15, 0.81, 0.74, -0.39, 0.45, 2.44, 0.59, -0.06, 0.09, 0.56, 0.65, 3.10, -0.44]
print("Day")
for x in range(1, 16):
    print(x)
print("Random Value")
for r in rand:
    print(r)
print("Time between Arrivas (IAT)")
for i in rand:
    IAT = mean + SD * i
    print(IAT)

print("Cumilative Arrival ")
x = 0
for i in range(0, len(rand)):
    x += (mean + SD * rand[i])
    print(x)
print("-----------------------------")
print("Normal Random ")
N_random = [0.59, -0.67, 0.41, 0.51, 1.53, -0.37, -0.27, - 0.15, -0.02, -1.60, -0.19, -0.16, -0.07, 0.24, -1.76]
for x1 in N_random:
    print(x1)

mean2 = 9.5
SD2 = 1

for x2 in N_random:
    x = mean2 + SD2 * x2
    print(x)

print("Service time")
cum = mean + SD * (rand[0])
servEnd = mean2 + SD2 * (N_random[0])
x = 0
total = cum + servEnd
x = (mean + SD * rand[0])
print(x)

for i in range(1, len(rand)):
    total += (mean + SD2 * (N_random[i - 1]))

    x += (mean + SD * rand[i])

    if x > total:
        print(x)


    else:
        print(total)

print("Service end Time")
cum = mean + SD * (rand[0])

servEnd = mean2 + SD2 * (N_random[0])

total = cum + servEnd

print(total)
for i in range(1, 15):
    total += (mean2 + SD2 * (N_random[i]))
    print(total)
print(f"Spend : {total}")

print("Wating Time ")

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
