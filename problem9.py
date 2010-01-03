#! /usr/bin/env python

from math import sqrt

def findTriplet():
    for a in range(1, 501):
        for b in range(1, 501):
            if a < b:
                c = sqrt(a**2 + b**2)
                if a + b + c == 1000:
                    return (a, b, int(c))

product = 1

for i in findTriplet():
    product *= i

print product