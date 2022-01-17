# Input format
# The first line contains T denoting the number of test cases.
# The first line of each test case containing an integer N  denoting the number of moves.
# Output format
# Print  lines. For each test case, print a single integer as described in the problem statement.

# Sample Input
# 1
# 1
# Sample Output
# 2

# He is initially at (0,0). He has 1 move to make, the positions where he can end up are (-1,0),(1,0) and (0,0).
# =abs(-1)+abs(0)+abs(1)+abs(0)+abs(0)+abs(0)
# =1+0+1+0+0+0
# =2

# We only need to calculate for x axis since y axis part will be zero.


t = int(input("Enter number of test cases: "))
for i in range(t):
    n = int(input("Enter number: "))
    print(n*(n+1))