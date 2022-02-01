# Sample Input
# 2
# 3 4
# 1 2 5
# 3 2
# 2 5 5
# Sample Output
# 3
# 0

n= int(input())
for _ in range(n):
    le,k  = map(int,input().split())
    array = list(map(int,input().split()))
    x = k-min(array)
    if x>0:
        print(x)
    else:
        print(0)