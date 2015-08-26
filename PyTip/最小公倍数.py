__author__ = 'zsh'

a = 3
b = 5


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def lcm(a, b):
    return a * b / gcd(a, b)


print lcm(a, b)
