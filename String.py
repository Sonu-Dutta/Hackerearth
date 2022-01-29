# Sample Input
# 5
# aaaaa
# Sample Output
# 0

from collections import Counter
 
def result(str):
    x = Counter(str)
    res = x.values()
    # print(res)
    return len(str)- max(res)
 
n = int(input())
str = input()
print(result(str))
