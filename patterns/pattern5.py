#PATTERN 5
# Input Format: N = 6
# Result:
# * * * * * *
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

def printTriangle(N):
        for i in range(N,0,-1):    #take range from reverse 5,4,3,2,1
            for j in range(i):
                print("*",end=" ")
            print()
N=int(input())
printTriangle(N)

