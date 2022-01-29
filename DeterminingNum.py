# Sample Input
# 8
# 1 2 3 4 5 5 3 4
# Sample Output
# 1 2

# Explanation
# The numbers other than 1 and 2 occur twice, hence, the answer is 1 and 2.

from collections import Counter

n = int(input())
arr = list(map(int,input().split()))
a = Counter(arr)
ans = []
for k,v in a.items():
    if v==1:
        ans.append(k)
        
ans.sort()       
print(*ans)

