#Exercise 1
from functools import reduce
num=[]
num_of_el=int(input("Number of elements in list:"))
for i in range(num_of_el):
    p=int(input("Elements:"))
    num.append(p)
mult=reduce(lambda x,y: x*y ,num )
print("Result of multiplication:",mult)



#Exercise 2
def n_of_u_l(a):
    b=0
    c=0
    for i in a:
        if i.isupper():
            b+=1
        elif i.islower():
            c+=1
    print("Number of upper case letters: ",b )
    print("Number of lower case letters: ",c)
a=input("Enter a sequence: ")
n_of_u_l(a)



#Exercise 3
a=input("Enter a word: ")
a=a.lower()
b="".join(reversed(a))
if a==b:
    print("It is palindrome")
else:
    print("It is not palindrome")



#Exercise 4
import time
import math
number = int(input()) 
delay = int(input())  
time.sleep(delay / 1000)
result = math.sqrt(number)
print(f"Square root of {number} after {delay} milliseconds is {result}")



#Exercise 5
def p_v(value):
    if value.lower() == "false":  
        return False
    elif value.lower() == "true": 
        return True
    else:
        return value 
a = ()
b = list(a)
c= int(input("Number of elements:"))
for i in range(c):
    p=input("Element:")
    b.append(p_v(p))
a=tuple(b)
print(all(a))