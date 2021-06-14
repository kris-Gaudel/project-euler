# Prime generator
def GeneratePrime(number):
    count = 1
    num = 1
    while (count < number):
        num += 2
        if PrimeTest(num):
            count += 1
    return num

# Prime tester


def PrimeTest(a):
    factor = 2
    while (factor * factor <= a):
        if a % factor == 0:
            return False
        factor += 1
    return True


print(GeneratePrime(10001))
