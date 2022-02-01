# Monk and Inversions
# Monk's best friend Micro, who happen to be an awesome programmer, got him an integer matrix M of size  for his birthday. Monk is taking coding classes from Micro. They have just completed array inversions and Monk was successful in writing a program to count the number of inversions in an array. Now, Micro has asked Monk to find out the number of inversion in the matrix M. Number of inversions, in a matrix is defined as the number of unordered pairs of cells  such that .
# Monk is facing a little trouble with this task and since you did not got him any birthday gift, you need to help him with this task.

# Video approach to solve this question: here

# Input:
# First line consists of a single integer T denoting the number of test cases.
# First line of each test case consists of one integer denoting N. Following N lines consists of N space separated integers denoting the matrix M.

# Output:
# Print the answer to each test case in a new line.

# Constraints:



# Sample Input
# 2
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# 2
# 4 3
# 1 4
# Sample Output
# 0
# 2
# Explanation
# In first test case there is no pair of cells , ,  having , so the answer is 0.
# In second test case  and , so the answer is 2.
for _ in range(int(input())):
    n = int(input())
    arr = []
    m = []
    l = []
    count = 0
    for k in range(n):
        arr.append(list(map(int, input().strip().split(" "))))
    for i in range(n):
        for j in range(n):
            m.append((i, j))
            l.append((i, j))
    for i, j in m:
        for p, q in l:
            if i <= p and j <= q:
                if arr[i][j] > arr[p][q]:
                    count += 1
    print(count)
    
    
    
    t = int(input())
for _ in range(t):
    n= int(input())
    matrix = []
    for i in range(n):
        a = list(map(int,input().split()))
        matrix.append(a)
        #print(matrix)
    c=0
    for i in range(n):
        for j in range(n):
            for p in range(n):
                for q in range(n):
                    if i<=p and j<=q:
                        if matrix[i][j]>matrix[p][q]:
                            c+=1
    print(c)