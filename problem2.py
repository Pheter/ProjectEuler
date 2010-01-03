#! /usr/bin/env python

fibonacci = [1, 2]

while fibonacci[-1] < 4000000:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

list = fibonacci
even = []

for i in list:
    if not i % 2:
        even.append(i)

sum = 0

for i in even:
    sum += i

print sum
