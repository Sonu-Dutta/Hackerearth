# Given two strings of equal length, you have to tell whether they both strings are identical.

# Two strings S1 and S2 are said to be identical, if any of the permutation of string S1 is equal to the string S2. See Sample explanation for more details.

# Input :

# First line, contains an intger 'T' denoting no. of test cases.
# Each test consists of a single line, containing two space separated strings S1 and S2 of equal length.
# Output:

# For each test case, if any of the permutation of string S1 is equal to the string S2 print YES else print NO.


# SAMPLE INPUT
# 3

# sumit mitsu

# ambuj jumba

# abhi hibb

# SAMPLE OUTPUT

# YES

# YES

# NO
from collections import Counter
def check(a,b):
    p = Counter(a)
    q = Counter(b)
    if sum((p-q).values())==0:
        print('YES')
    else:
        print('NO')

n = int(input())
for _ in range(n):
    a,b = input().split()
    check(a,b)





