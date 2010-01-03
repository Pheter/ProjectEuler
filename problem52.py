#! /usr/bin/env python

def compareDigits(number1, number2):
    number1 = str(number1)
    number2 = str(number2)
    
    for i in number1:
        found = False
        tmp_len = len(number2)
        for j in range(0, len(number2)):
            if found == False:
                if i == number2[j]:
                    tmp = ''
                    for k in range(0, len(number2)):
                        if k != j:
                            tmp += number2[k]
                    number2 = tmp
                    found = True
        if tmp_len != len(number2) + 1:
            break
    
    if len(number2) == 0:
        return True
    else:
        return False

i = 1
solved = False
while solved == False:
    if compareDigits(i, i*6):
        if compareDigits(i, i*5):
                if compareDigits(i, i*4):
                    print i
                    solved = True
    i += 1