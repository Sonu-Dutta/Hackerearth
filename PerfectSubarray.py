# You are given an array  of  integers. You need to count the subarrays which have the sum of all elements in it a perfect square.

# Input
# The first line contains an integer  that denotes count of elements in the array. Next line contains  space separated integers that denote elements of the array.

# Output
# In the output, you need to print the count of subarrays for which the sum of elements is a perfect square.

# Constraints

# Sample Input
# 4
# 1 4 2 3
# Sample Output
# 3

# Explanation
# The given array is: 1 4 2 3

# Let us list the sum of all possible subarrays:

# [1 , 1] = 1
# [1 , 2] = 1 + 4 = 5
# [1 , 3] = 1 + 4 + 2 = 7
# [1 , 4] = 1 + 4 + 2 + 3 = 10
# [2 , 2] = 4
# [2 , 3] = 4 + 2 = 6
# [2 , 4] = 4 + 2 + 3 = 9
# [3 , 3] = 2
# [3 , 4] = 2 + 3 = 5
# [4 , 4] = 3

# [1, 4, 9] = 3

import math
n = int(input())
l = list(map(int,input().split()))

def checkperfect(n):
    i = int(math.sqrt(n))
    if n==i*i:
        return True
    else:
        return False


c=0
for i in range(n):
    s= 0
    for j in range(i,n):
        s+=l[j]
        if checkperfect(s):
            c+=1
print(c)