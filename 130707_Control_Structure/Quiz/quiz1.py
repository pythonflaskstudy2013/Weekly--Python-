#!/usr/bin/python

def commify(number, n = 3):
    reversed_number = number[::-1]
    splited_number = [reversed_number[i:i+n] for i in range(0, len(reversed_number), n)]
    return ','.join(splited_number)[::-1]

data = '1'
for i in range(100):
    data = data + '0'
    print commify(data)
