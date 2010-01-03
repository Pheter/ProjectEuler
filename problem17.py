word_list = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def getWord(n):
    if n == 0:
        return ''
    if n >= 1:
        if n <= 19:
            return word_list[n]
        elif n <= 99:
            return word_list[int(str(n)[0])*10] + getWord(int(str(n)[1]))
        elif n <= 999:
            if str(n)[1:3] == '00':
                return word_list[int(str(n)[0])] + 'hundred' + getWord(int(str(n)[1:3]))
            else:
                return word_list[int(str(n)[0])] + 'hundredand' + getWord(int(str(n)[1:3]))
        elif n == 1000:
            return 'onethousand'
    return False

words = ''
for i in range(1, 1000 + 1):
    words += getWord(i)

print len(words)
