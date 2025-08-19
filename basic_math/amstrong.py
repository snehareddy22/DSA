#Check if a number is Armstrong Number or not
# Problem Statement: Given an integer N, return true it is an Armstrong number otherwise return false.
# An Amrstrong number is a number that is equal to the sum of its own digits each raised to the power of the number
# of its own digits

def amstrongNum(num):
    original_num= num       # Store the original number
    num_digits = len(str(num))    # Find the number of digits
    armstrong_sum = 0            # Initialize sum
# Calculate the sum of digits raised to the power of num_digits
    while num > 0:
        digit = num % 10
        armstrong_sum += digit ** num_digits #like 123 then digit to the power of 3
        num //=10                       #removes last digit and continue iteration
    if armstrong_sum == original_num:
        print("is an Armstrong number:",original_num)
    else:
        print("is not an Armstrong number:",original_num)
num=int(input("enter a number:"))
amstrongNum(num)
       