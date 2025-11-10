#Set Matrix Zero
def setZeroes(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    # Step 1: mark with -1
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                # mark row
                for k in range(cols):
                    if matrix[i][k] != 0:
                        matrix[i][k] = -1
                # mark column
                for k in range(rows):
                    if matrix[k][j] != 0:
                        matrix[k][j] = -1             
    # Step 2: replace -1 with 0
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

# Time Complexity: O((n × m) × (n + m))
#space complexity : O(1)


#better approach(creating two new arrays)
def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    row = [0] * n
    col = [0] * m
    # Step 1: mark rows & cols that have zeros
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row[i] = 1
                col[j] = 1
    # Step 2: set cells to zero if their row/col is marked
    for i in range(n):
        for j in range(m):
            if row[i] == 1 or col[j] == 1:
                matrix[i][j] = 0
# Time Complexity:  O(n × m) 
#space complexity: O(n + m)


#optmial approach
def setZeroes(matrix):
    n = len(matrix)
    m = len(matrix[0])
    firstRowZero = False
    firstColZero = False
    # Step 1: check if first row or first column have any zeros
    for j in range(m):
        if matrix[0][j] == 0:
            firstRowZero = True
    for i in range(n):
        if matrix[i][0] == 0:
            firstColZero = True
    # Step 2: mark rows & cols using first row and col
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0
    # Step 3: set cells to zero based on marks
    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0
    # Step 4: zero the first row & first column if needed
    if firstRowZero:
        for j in range(m):
            matrix[0][j] = 0
    if firstColZero:
        for i in range(n):
            matrix[i][0] = 0

# Time Complexity: O(n × m)
# Space Complexity: O(1) — no extra arrays used
