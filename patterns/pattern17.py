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
        for j in range(i):
            print(chr(i - 1, -1, -1):, end='')
        print()
N = int(input())
print_pyramid_palindrome(N)


# *    *
# **  **
# ******
# ******
# **  **
# *    *
N = 3  # number of rows for each half

# Upper half
for i in range(1, N+1):
    print("*" * i, end="")        # left wing
    print(" " * (2*(N-i)), end="") # spaces
    print("*" * i)                # right wing

# Lower half
for i in range(N, 0, -1):
    print("*" * i, end="")        # left wing
    print(" " * (2*(N-i)), end="") # spaces
    print("*" * i)                # right wing
