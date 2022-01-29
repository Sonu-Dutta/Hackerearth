# Sample Input
# 6
# 1 1 1 2 2 0
# 6
# 1
# 2
# 1
# 0
# 3
# 4
# Sample Output
# 3
# 2
# 3
# 1
# NOT PRESENT
# NOT PRESENT

# Explanation
# The given array is (1,1,1,2,2,0) of size 6.

# Total number of queries is 6 also.

# For the first query i.e for 1 , the total of number of occurrences of 1 in the given array is 3 . Hence the corresponding output is 3.

# For the second query i.e. for 2, the total of number of occurrences of 2 in the given array is 2 . Hence the corresponding output is 2.

# For the fifth query i.e. for 3. 3 is not present in the array . So the corresponding output is "NOT PRESENT" (without quotes).

from collections import Counter
n= int(input())
a = list(map(int,input().split()))
m = int(input())
p = Counter(a)

for i in range(m):
    x = int(input())
    if p[x]:
        print(p[x])
    else:
        print('NOT PRESENT')