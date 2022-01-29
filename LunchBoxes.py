
# Sample Input
# 2
# 10 4
# 3 9 4 2
# 5 6
# 3 2 1 1 2 1
# Sample Output
# 3
# 4

# Explanation
# In first test case 1,3,4 schools got lunch-boxes.
# In second test case 3,4 and 2(or 5) schools got lunch boxes.

for i in range(int(input())):
    co=0
    n,m=map(int,input().split())
    li=[int(x) for x in input().split()]
    li.sort()
    for i in li:
        if i<=n:
            n-=i
            co+=1
        else:
            break
    print(co)