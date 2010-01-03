#! /usr/bin/env python

sum = 0

for i in range(0, 1000, 5):
        sum += i

for i in range(0, 1000, 3):
    if i not in range(0, 1000, 5):
        sum += i

print sum