'''
Find GCD of two numbers
Problem Statement: Given two integers N1 and N2, find their greatest common divisor.
The Greatest Common Divisor of any two integers is the largest number that divides both integers.
'''

#brute force solution
def find_gcd(n1,n2):
    gcd=1   
    for i in range(1,min(n1,n2)+1):       #Iterate from 1 up to the minimum of n1 and n2
        if n1 % i == 0 and n2 % i == 0:   #if the divisors are same
            gcd=i                         #gcd is that numer
    return gcd
n1=int(input())
n2=int(input())
print(find_gcd(n1,n2))
#TC=O(min(n1, n2))
#SC=O(1)


#euclids algorithm
def gcd(a,b):
    while a!=b:
        if a>b:
            a=a-b
        else:
            b=b-a
    return a        #becouse a and b are equal now a=a-b,b=b-a return same value 
a=int(input())
b=int(input())
print(gcd(a,b))
#TC=O(max(a,b))
#SC=O(1)

#recursion way
def gcd(a,b):
    if b==0:
        return 0
    return gcd(b,a%b)
a=int(input())
b=int(input())
print(gcd(a,b))
#TC=O(log min(a, b))
#SC=O(log min(a, b))

#optimised way
def gcd(a,b):
    while b!=0:
        a,b=b,a%b
    return a
a=int(input())
b=int(input())
print(gcd(a,b))
#TC=O(log min(a,b))
#SC=O(1)