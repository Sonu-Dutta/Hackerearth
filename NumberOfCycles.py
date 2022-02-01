# Sample Input
# 2
# 3
# 4
# Sample Output
# 7
# 13
t = int(input("Enter number of test cases: "))
for _ in range(t):
    n = int(input("Enter number of sides: "))
    ans = 1
    ans += (n-1)*n
    print(ans)