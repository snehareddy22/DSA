# Pattern - 16: Alpha-Ramp Pattern
# Input Format: N = 6
# Result:   
# A 
# B B
# C C C
# D D D D
# E E E E E
# F F F F F F
# Function to print the alphabet pattern
def print_alphabet_pattern(N):
    for i in range(N):
        ch = chr(65 + i)  # ASCII value of 'A' is 65
        for j in range(i + 1):
            print(ch, end=" ")
        print()
# Example: input
N = int(input("Enter N: "))
print_alphabet_pattern(N)

