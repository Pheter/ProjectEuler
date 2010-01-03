#! /usr/bin/env python

import re

sum = 0
for x in range(1, 1001):
    y = x**x
    sum += y

print 'Last 10 digits of sum: ', re.findall('\d{10}$', str(sum))