# Sample Input
# 3
# 3 2 4 2
# 3 3 6 3
# 3 3 4 3
# Sample Output
# Yes
# Yes
# No

I = int(input())
for i in range(I):
    x,y,a,b = map(int,input().split())
    if (x*y) == a+b:
        print("Yes")
    else:
        print("No")