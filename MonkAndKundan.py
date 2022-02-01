# Problem
# Kundan being a good friend of Monk, lets the Monk know that he has a following string Initial which consists of the following letters in the mentioned order: "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ".

# He also has various lists of strings, and now he wants the Monk to compute the Hash value of each list of strings.
# Here's the following algorithm used by the Monk to do it.
# So, the Hash is the summation of all the character values in the input:
# (currentIndex + (position of the character In the string initial) ). And then this hash is multiplied by the Number of strings in the list.

# Let's assume that the list of strings is: ["aA1", "b"]. So, our answer would be:
# a: 0 + 0 = 0.
# A: 1 +  = .
# 1: 2 +  = .
# b: 0 + 1 = 1.

# So, 2 * (0 + 1 +  + ) = 2 * () = .

# Input format:
# The first line contains an integer T, denoting the number of test cases. For every test case, on a single line, there will be N number of strings all of them separated by a space, denoting all the strings of that particular list of strings.

# Output format:
# Print the required hash for each of the mentioned list of strings.

# Note:
# All the characters in the input will be valid, that is, will be part of the string Initial.

# Sample Input
# 3
# aA1 b
# a b c d
# aa BB cc DD
# Sample Output
# 132
# 24
# 640



def index(ref,x):
    for i in range(len(ref)):
        if ref[i]==x:
            return i
            
ref = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ref  = list(ref)
n = int(input())
for i in range(n):
    l = list(input().split())
    print(l)
    s=0
    for i in range(len(l)):
        for j in range(len(l[i])):
            t= index(ref,l[i][j])
            s+=j+ t
    print(s*len(l))