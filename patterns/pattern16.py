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
        # Get the corresponding uppercase letter (A, B, C, ...)
        letter = chr(65 + i)  # 65 is ASCII value for 'A'
        # Print the letter i+1 times separated by space
        print((letter + ' ') * (i + 1))
N = int(input())
print_alphabet_pattern(N)

