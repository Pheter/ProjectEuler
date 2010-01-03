#! /usr/bin/env python

import re

data = []

with open('problem67.txt') as file:
    for line in file:
        fixed_values = re.sub(' 0', ' ', line)
        data.append([int(i) for i in fixed_values.split()])

while len(data) >= 2:
    for i in range(0, len(data[len(data) - 1]) - 1):
        data[len(data) - 2][i] = data[len(data) - 2][i] + max([data[len(data) - 1][i], data[len(data) - 1][i + 1]])
    data.pop()

print data