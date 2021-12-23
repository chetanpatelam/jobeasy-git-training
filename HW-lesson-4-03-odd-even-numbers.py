import math
from random import randint
number = 0
odd = 0
even = 0
number = input('Enter any 5 digit number :')
number = int(number)
temp = 0

while number != 0:
    temp = number % 10
    if temp % 2 == 0:
      even = even + temp
    else:
        odd = odd + temp


    number = number // 10
    temp = 0

print(f'Total of all odd numbers is : {odd}')
print(f'Total of all even numbers is : {even}')

