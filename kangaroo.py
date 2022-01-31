# Sample Input
# 3
# 1 10 2
# 5 10 3
# 7 9 5

# Sample Output
# 5
# 2
# 0

# Explanation
# Test Case #1:
# There are 5 multiples of 2 that are {2,4,6,8,10} in range [1,10] .

# Test Case#2:
# There are 2 multiples of 3 that are {6,9} in range [5,10] .

# Test Case#3: There are no any multiple of 5 is there in range [7,9].
t = int(input())
for _ in range(t):
    a,b,m = map(int,input().split())
    ans =0 
    for i in range(a,b+1):
        if i%m == 0 :
            ans +=1
    print(ans)