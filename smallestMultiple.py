def isValid(number):
    for i in range(2,21):
        if number % i != 0:
            return False
    return True

n = 2520
while True:
    if isValid(n):
        break
    n+=2520

print(n)