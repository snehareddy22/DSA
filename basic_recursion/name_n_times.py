#Print Name N times using Recursion
def func(i,n):   #i=store current value   n stores total times to print
#base condition
    if i>n:
        return
#work
    print("sneha")
#recursive calling
    func(i+1,n)
#driver code
n=int(input())
func(1,n)          
#func(1, n) → prints once → calls func(2, n)
#func(2, n) → prints once → calls func(3, n) … until i > n, then recursion stops.