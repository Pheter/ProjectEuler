import math

def isPentagonal(x):
    n = (math.sqrt(24 * x + 1) + 1) / 6
    if n == int(n):
        return True
    return False

n = 144
found = False

while not found:
    i = n * ((2 * n) - 1)
    if isPentagonal(i):
        print i
        found = True
    n += 1