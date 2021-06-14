import math


def factors(n):
    factorsArray = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factorsArray.append(i)
            factorsArray.append(n // i)
    return factorsArray


def primeTest(n):
    return len(factors(n)) == 2


factorsOfNum = factors(600851475143)
largestPrime = 0
for factor in factorsOfNum:
    if (primeTest(factor) and factor > largestPrime):
        largestPrime = factor

print(largestPrime)
