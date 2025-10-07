#Print Name N times using Recursion
def func(name,n):   #n is total times to print
    if n==0:        #base condition
        return 
    print(name)     
    func(name,n-1)  #recursive calling
n=int(input())      #driver code
func("sneha",n)        
'''
Sneha   # n=5
Sneha   # n=4
Sneha   # n=3
Sneha   # n=2
Sneha   # n=1
recusrion stops calling at n=0
'''

#TC=O(N)
#SC=O(N)
