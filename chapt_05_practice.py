
'''
# Q1

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class UpgradeCalculator(Calculator):
#    def __init__(self):
#        self.value = 0

    def minus(self, val):
        self.value -= val


cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print(cal.value)
'''

'''
# Q2

class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val


class MaxLimitCalculator(Calculator):
    def add(self, val):
        self.value += val
        if (self.value >= 100):
            self.value = 100

cal = MaxLimitCalculator()
cal.add(50)
cal.add(60)

print(cal.value)
'''

'''
# Q4

print(list(filter(lambda x:x>0, [1, -2, 3, -5, 8, -3])))
'''

'''
# Q5

print(int('0xea', 16))
'''

'''
# Q6

print(list(map(lambda x:x*3, [1, 2, 3, 4])))
'''

'''
# Q7

a = [-8, 2, 7, 5, -3, 5, 0, 1]

print(max(a) + min(a))
'''

'''
# Q8

print(round(17/3, 4))
'''

# Q9


'''
import sys

list_len = len(sys.argv) - 1

sum = 0
i = 1

if (list_len != 0):
    while (list_len > 0):
        sum += int(sys.argv[i])
        list_len -= 1
        i += 1

print(sum)
'''
'''
import sys

numbers = sys.argv[1:]

result = 0

for number in numbers:
    result += int(number)

print(result)
'''

# Q10

'''
import os

os.chdir("C:/doit")

result = os.popen("dir")

print(result.read())
'''

# Q11

# Q12

'''
import time

print(time.strftime("%Y/%m/%d %H:%M:%S"))
'''

# Q13

import random

result = []

while (len(result) < 6):
    num = random.randrange(1, 46)
    if num not in result:
        result.append(num)


print(result)