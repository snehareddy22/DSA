#Pattern - 17: Alpha-Hill Pattern
#      A     
#     ABA    
#    ABCBA   
#   ABCDCBA  
#  ABCDEDCBA 
# ABCDEFEDCBA
def print_pyramid_palindrome(N):
    for i in range(1, N + 1):
        # Print leading spaces
        print(' ' * (N - i), end='')

        # Print ascending letters
        for j in range(i):
            print(chr(65 + j), end='')

        # Print descending letters
        for j in range(i - 2, -1, -1):
            print(chr(65 + j), end='')

        # Move to next line
        print()
N = int(input())
print_pyramid_palindrome(N)
