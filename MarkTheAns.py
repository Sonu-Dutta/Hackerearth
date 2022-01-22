
n,k = map(int,input("Enter number of questions and max_difficulty: ").split())
l = list(map(int,input("Enter integers according to it's difficulty level:  ").split()))
c=0
skip=0
for i in range(n):
    if l[i]<=k and skip<2:
        c+=1
    else:
        skip+=1
print(c)