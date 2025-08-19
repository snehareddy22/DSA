#Check if a number is prime or not
# Problem Statement: Given an integer N, check whether it is prime or not. A prime number is a number that
# is only divisible by 1 and itself and the total number of divisors is 2.
def check_Prime(n):
    count=0
    for i in range(1,n+1):    #checks from 1 to n
        if n%i==0:            #check is n divisible by i or not
            count=count+1     #if divisible count increases
    if count==2:             #prime number has only 2 divisors (1 and itslef)
        print("it is a prime number")
    else:
        print("it is not a prime number")
n=int(input())
check_Prime(n)
