
# Sample Input
# 2
# 3
# 3 1 2
# 3
# 1 2 3
# Sample Output
# not inverse
# inverse

for x in range(int(input())):
     n=int(input());l=list(map(int,input().split()));a=[0]*n
     for x in range(n):
          a[l[x]-1]=x+1
     if(a==l):print("inverse")
     else:print("not inverse")