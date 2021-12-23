import math
from random import randint
number = 0
total = 0
number = input('Enter any multi digit number :')
number = int(number)
temp = 0

while number != 0:
    temp = number % 10
    total = total + temp
    number = number // 10
    temp = 0

print(f'Total of all numbers is : {total}')

