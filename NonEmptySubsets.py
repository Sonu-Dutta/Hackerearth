
# Sample Input
# 2
# 4
# 1 3 5 7
# 3
# 2 6 14
# Sample Output
# 1
# 2


n=int(input())
i=1
while(i<=n):
    n1=int(input())
    l=list(map(int,input().split()))
    print(min(l))
    i+=1