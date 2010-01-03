#! /usr/bin/env python

k = 0
i = 20

while k < 9:
    i += 20
    k = 0

    for j in range(11, 20):
        if not i % j:
            k += 1

    if k is 9:
        print i