def factorialOfParNum(n):
    if n % 2 != 0:
        return "The number is impair, GG"
    if n < 0:
        return 0
    elif n < 2:
        return 1
    else:
        fact = 2
        while (n > 2):
            fact *= n
            n -= 1
        return fact


result = factorialOfParNum(6)
print(result)