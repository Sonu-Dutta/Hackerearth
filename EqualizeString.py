# You are given two binary strings  and  and are required to make  equals to . There are two types of operations:

# Swap any two adjacent bits or characters in string . The cost of this operation is 1 unit.
# Flip the bit or character of the string. The cost of this operation is 1 unit.
# What is the minimum cost to make string  equal to ?

# Input format
# The first line contains one integer that denotes the length of both strings.
# The next two lines take two strings  and  of length  as an input.
# Output format
# Print one integer that represents the minimum cost required to convert string  to string .
# The length of both the strings  and  is always the same.

# Sample Input
# 4
# 1101
# 0011

# Sample Output
# 2

# Explanation
# We will flip the first character which will cost us 1 unit. Now the string A will be "0101".
# We will swap second and third characters which will also cost us 1 unit.
# Now the string A will be "0011" which is same as B. Hence our total cost will be 2 units will be optimal.  
n = int(input())
s = list(input())
p = list(input())
ans = 0
for i in range(0, n - 1):
    if s[i] == p[i + 1] and s[i + 1] == p[i] and s[i] != s[i + 1]:
        s[i], s[i + 1] = s[i + 1], s[i]
        ans += 1
print(ans + sum(s[i] != p[i] for i in range(n)))