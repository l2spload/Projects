#The provided code stub reads two integers from STDIN,  and . Add code to print three lines where:
#The first line contains the sum of the two numbers.
#The second line contains the difference of the two numbers (first - second).
#The third line contains the product of the two numbers.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a + b)
print(a - b)
print(a * b)


#The provided code stub reads two integers,  and , from STDIN.
#Add logic to print two lines. The first line should contain the result of integer division,  // . The second line should contain the result of float division,  / .
#No rounding or formatting is necessary.

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    
print(a//b)
print(a/b)


#The provided code stub reads and integer, n, from STDIN. For all non-negative integers i < n, print i**2.

for i in range(0, n):
    print(i)

i = 0
while i < n:
    print(i)
    i += 1


#In the Gregorian calendar, three conditions are used to identify leap years:
#The year can be evenly divided by 4, is a leap year, unless:
#The year can be evenly divided by 100, it is NOT a leap year, unless:
#The year is also evenly divisible by 400. Then it is a leap year.

def is_leap(year):    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False

year = int(input())
print(is_leap(year))


#The included code stub will read an integer, , from STDIN.
#Without using any string methods, try to print the following:
#123...n
#Note that "..." represents the consecutive values in between.

if __name__ == '__main__':
    n = int(input())
    
for i in range(1,n+1):
    print (i, end='')


#Given an integer, , perform the following conditional actions:
#If  is odd, print Weird
#If  is even and in the inclusive range of  to , print Not Weird
#If  is even and in the inclusive range of  to , print Weird
#If  is even and greater than , print Not Weird

if (n % 2 != 0):
    print('Weird')
elif (n % 2 == 0 and 2 < n < 5):
    print('Not Weird')
elif (n % 2 == 0 and 6 < n < 20):
    print('Weird')
elif (n % 2 == 0 and n > 20):
    print('Not Weird')


# You are given three integers representing the dimensions of a cuboid along with an integer. 
# Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to.

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    print([[a, b, c] for a in range(0,x+1) for b in range(0,y+1) for c in range(0,z+1) if a + b + c != n])


# Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

if __name__ == '__main__':
    marksheet = []
    scorelist = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scorelist+=[score]
        
    sort_list = sorted(list(set(scorelist)))[1]
    
    for score_output,score_sheet in sorted(marksheet):
        if sort_list==score_sheet:
            print(score_output)



# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.


if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))


# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    res=''
    for i in s:
        if i.islower():
            res+=i.upper()
        else:
            res+=i.lower()
    return res

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)


# Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

if __name__ == '__main__':
    regular_list = []
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    for n in integer_list:
        regular_list.append(n)
    tuple_list = tuple(regular_list)
    print(hash(tuple_list))


#

if __name__ == '__main__':
    N = int(input())
    m=[]
    for _ in range(N):
       method,*l=input().split()
       k=list(map(int,l))
       if len(k)==2:
          q=[k[0]]
          w=[k[1]]
       elif len(k)==1:
          q=[k[0]]
       if method =='insert':
          m.insert(q[0],w[0])
       elif method == 'append':
          m.append(q[0])
       elif  method == 'remove':
          m.remove(q[0])
       elif method =='print':
          print(m)
       elif method == 'reverse':
          m.reverse()
       elif method =='pop':
          m.pop()
       elif method == 'sort':
          m.sort()


# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    split_input = line.split(" ")
    joined_input = "-".join(split_input)
    return joined_input
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)


#Complete the print_full_name function in the editor below.
#print_full_name has the following parameters:
#string first: the first name
#string last: the last name

def print_full_name(first, last):
    print('Hello {first} {last}! You just delved into python.'.format(first=first,last=last))

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)


#