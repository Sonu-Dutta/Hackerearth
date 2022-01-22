
n,m = map(int,input("Enter total elements(n) and the number on adding 2 values(m): ").split())
arr = list(map(int,input("Enter elements: ").split()))

count=0
for i in range(n):
    for j in range(i+1,n):
        summ=arr[i]+arr[j]
        
        if(summ==m):
            count+=1
print(count)
        