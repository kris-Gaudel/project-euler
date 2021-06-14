valid = []
sum = 0
for i in range (0, 1000):
    if (i % 3 == 0 or i % 5 == 0):
        valid.append(i)

for i in range(0, len(valid)):
    sum += valid[i]
    print(sum)