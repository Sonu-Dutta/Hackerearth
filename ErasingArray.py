
# Sample Input
# 3
# 4
# 0 0 1 1
# 2
# 1 0
# 2
# 0 0
# Sample Output
# 1
# 2
# 1

# Explanation
# First test case: Entire array can be deleted in one operation as [0,0,1,1] has no inversions.

# Second test case: You can delete the entire array in two operations in first [1] and in second [0], you can not do it one as [1,0] has inversions.

# Third test case: You can do this in one operation as array includes no inversions.

# Note: You always need to delete the subarray from 0th index (0-based indexing).

t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int,input().split()))
    c = 1
    for i in range(n-1):
        if arr[i] == 1 and arr[i+1]==0:
            c+=1
    print(c)