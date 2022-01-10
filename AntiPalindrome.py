# You are given a string  containing only lowercase alphabets. You can swap two adjacent characters any number of times (including 0).

# A string is called anti-palindrome if it is not a palindrome. If it is possible to make a string anti-palindrome, then find the lexicographically smallest anti-palindrome. Otherwise, print .

# Input format

# The first line contains a single integer  denoting the number of test cases. The description of  test cases follows.
# Each line contains a string  of lower case alphabets only.
# Output format

# For each test case, print the answer in a new line.

# Sample Input
# 4
# bpc
# pp
# deep
# zyx
# Sample Output
# bcp
# -1
# deep
# xyz

t = int(input("Enter number of test cases: "))
for i in range(t):
    inp = input("Enter the string: ")
    s = ''.join(sorted(inp))
    if s == s[::-1]:
        print(-1)
    else:
        print(s)