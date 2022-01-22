testCase  = int(input("Enter number of test cases: "))
for _ in range(testCase):
    n = int(input("Enter number of cars: "))
    l = list(map(int,input("Enter car speed: ").split()))
    c=1
    ms = l[0]
    
    for i in range(1,n):
        if l[i]<=ms:
            c+=1
            ms = l[i]
    print(c)