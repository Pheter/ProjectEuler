#! /usr/bin/env python

n = 100
factorial = n

while n > 1:
    n -=1
    factorial *= n

factorial = str(factorial)
sum = 0

for i in factorial:
    sum += int(i)

print sum