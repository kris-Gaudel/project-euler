f1 = 1
f2 = 1
fth = 0
evenSum = 0

while fth <= 4000000:
    if fth % 2 ==0:
        evenSum += fth
    f1 = f2
    f2 = fth
    fth = f1 + f2

print(evenSum)
