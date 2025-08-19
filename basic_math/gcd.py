#Find GCD of two numbers
#Problem Statement: Given two integers N1 and N2, find their greatest common divisor.
#The Greatest Common Divisor of any two integers is the largest number that divides both integers.
def find_gcd(n1,n2):
    gcd=1   #This variable will store the greatest common divisor of the input numbers n1 and n2.
    for i in range(1,min(n1,n2)+1): #Iterate from 1 up to the minimum of n1 and n2
        if n1 % i == 0 and n2 % i == 0:   #if the divisors are same
            gcd=i
    return gcd
n1=int(input())
n2=int(input())
print(find_gcd(n1,n2))

