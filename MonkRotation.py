# Input:
# The first line will consists of one integer T denoting the number of test cases.
# For each test case:
# 1) The first line consists of two integers N and K, N being the number of elements in the array and K denotes the number of steps of rotation.
# 2) The next line consists of N space separated integers , denoting the elements of the array A.

# Sample Input
# 1
# 5 2
# 1 2 3 4 5
# Sample Output
# 4 5 1 2 3
testCase  = int(input())
for _ in range(testCase):
    n,k = map(int,input().split())
    l = list(map(int,input().split()))
    x = k%n
    print(*(l[n-x:]+l[:n-x]))