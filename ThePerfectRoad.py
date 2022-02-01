# Given that, there are N paths numbered from 1 to N, where each path connects the starting point S to the destination point X. The maximum speed limit is speed[i] for the  path which can be used to reach the destination. Find the path to reach the destination as early as possible. If there are multiple paths from which you can choose, print Many Roads. Also, it is guaranteed that X will always be greater than S.
# Input format:
# First line will contain the number of test cases T.
# Each test case will be as follows:
# First line consists of S, X and N, which denotes the starting point, destination point and number of paths respectively.
# Next line will contain N numbers that denote maximum speed limit of the paths.
# Output Format:
# For each test case, output a single integer denoting the path chosen to reach the destination as early as possible. If there are multiple paths from which you can choose, you have to output "Many Roads" without quotes.

# Input Constraints:

# Sample Input
# 2
# 5 65 3
# 75 35 40
# 0 40 4
# 50 50 10 20
# Sample Output
# 1
# Many Roads

# Source Limit:
# Explanation
# In the first sample case, the time taken to reach X is the minimum from the 1st path and in the second case, both 1st and 2nd paths require equal time to reach X.
t=int(input())
for i in range(0,t):
    z=input()
    s,x,n=z.split()
    s=int(s)
    x=int(x)
    n=int(n)
    y=input()
    l=y.split()
    for j in range(0,len(l)):
        l[j]=int(l[j])
    zz=max(l)
    ctr=0
    for j in range(0,len(l)):
        if l[j]==zz:
            ctr+=1
    if ctr==1:
        for j in range(0,len(l)):
            if l[j]==zz:
                print(j+1)
                break
    else:
        print("Many Roads")
        