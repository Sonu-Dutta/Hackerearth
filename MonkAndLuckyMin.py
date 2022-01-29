# Sample Input
# 2
# 5
# 8 8 9 5 9
# 5
# 3 3 3 5 3
# Sample Output
# Lucky
# Unlucky

# Explanation
# In first case, value of minimum element is 5 and it's frequency is 1 which is odd, so the array is Lucky.
# In second case, value of minimum element is 3 and it's frequency is 4 which is even, so the array is Unlucky.
testCase  = int(input())
from collections import Counter
for _ in range(testCase):
    n = int(input())
    l = list(map(int,input().split()))
    p  = Counter(l)
    x = min(l)
    if p[x]%2==0:
        print('Unlucky')
    else:
        print("Lucky")