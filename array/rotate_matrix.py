#Rotate Image or rotate matrix
def rotate(matrix):
    n=len(matrix)
    result = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            result[j][n-i-1]=matrix[i][j]
    #for in place rotation lc type if needed
    for i in range(n):
        for j in range(n):
            matrix[i][j]=result[i][j]

    return matrix
# Complexity
# Time: O(n²) — we visit every cell once.
# Space: O(n²) — new matrix used for rotated version.



def  rotate(matrix):
    n=len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]  #traspose the matrix
    for i in range(n):
        matrix[i].reverse()

    return matrix
# Complexity
# Time: O(n²) 
# Space: O(1) 