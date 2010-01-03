#! /usr/bin/env python

def includes_factor(list, i):
    for prime in primes:
        if not i % prime:
            return True

primes = [2]
i = 3

while primes.__len__() < 10001:
    if not includes_factor(primes, i):
        primes.append(i)
    i += 2

print primes