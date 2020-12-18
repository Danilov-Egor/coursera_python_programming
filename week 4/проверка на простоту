from math import sqrt
n = int(input())


def IsPrime(n):
    i = 2
    while n % i != 0:
        i += 1
        if i > sqrt(n):
            return True
    if n == 2:
        return True
    elif i > 1:
        return False


if IsPrime(n):
    print('YES')
else:
    print('NO')
