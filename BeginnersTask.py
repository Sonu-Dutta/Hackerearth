t=int(input())
for i in range(t):
    n=int(input())
    a=list(input().split())
   
    c=0
    for j in range(n):
        if(int(a[j])%2==0):
            c=c+1
    print(c)