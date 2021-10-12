# Day 0

input_string = input()
print('Hello, World.')


# Day 1

i = 4
d = 4.0
s = 'HackerRank '

test_int = int(input())
test_doub = float(input())
test_string = str(input())

print(i + test_int)
print(d + test_doub)
print(s + test_string)


# Day 2

def solve(meal_cost, tip_percent, tax_percent):
    print(int(round(meal_cost + ((tip_percent/100) * meal_cost) + ((tax_percent/100) * meal_cost))))
    return 0

##########################################################

def solve(meal_cost, tip_percent, tax_percent):
    meal_tip = (meal_cost + ((tip_percent/100) * meal_cost))
    meal_tax = ((tax_percent/100) * meal_cost)
    print(int(round(meal_tip + meal_tax)))
    return 0


# Day 3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())
    if (N % 2 != 0):
        print('Weird')
    elif ((N % 2 == 0) and (N in range(6, 21))):
        print('Weird')
    elif ((N % 2 == 0) and (N in range(2,6))):
        print('Not Weird')
    elif ((N % 2 == 0) and (N > 20)):
        print('Not Weird')


# Day 4

class Person:
    def __init__(self,initialAge):
        if initialAge > 0:
            self.age = initialAge
        else:
            self.age = 0
            print('Age is not valid, setting age to 0.')

    def amIOld(self):
        if self.age < 13:
            print('You are young.')
        elif self.age >= 13 and self.age < 18:
            print('You are a teenager.')
        else:
            print('You are old.')

    def yearPasses(self):
        self.age += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")


# Day 5

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    for num in range(1,11):
        total = n * num
        print("{n} x {num} = {total}".format(n=n,num=num,total=total))


# Day 6

num = int(input()) 

string_list = [] 

for n in range(num): 
    element = input() 
    string_list.append(element)

for i in string_list: 
    print(i[::2],i[1::2])


# Day 7

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    print(' '.join(map(str, arr[::-1])))

####################################################

import math
import os
import random
import re
import sys

num_list = []

if __name__ == '__main__':
    for n in arr[::-1]:
        num_list.append(str(n))
        
print(' '.join(num_list))



# Day 8

list_input=int(input())

dct={}

for i in range(list_input):
    j=input()
    dat=j.split()
    p=dat[0]
    q=dat[1]
    dct[p]=q
k=input()

while(k!=None):
    
    if(k in dct):
        print (k +'='+ dct[k])
    else:
        print("Not found")
    try:
        k=input()
    except:
        k=None



# Day 9

#!/bin/python3

import math
import os
import random
import re
import sys

def factorial(n):
    if n <= 1:
        return 1
    else:
        result = n * factorial(n - 1)
        return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
