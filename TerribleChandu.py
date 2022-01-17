# Chandu is a bad student. Once his teacher asked him to print the reverse of a given string. He took three hours to solve it. 
# The teacher got agitated at Chandu and asked you the same question. Can you solve it?
# Input:
# The first line contains an integer T, denoting the number of test cases.
# Each test case contains a string S, comprising of only lower case letters.
# Output:
# For each test case, print the reverse of the string S.

# Sample Input
# 2
# ab
# aba
# Sample Output
# ba
# aba

n = int(input("Enter number of test cases: "))
for i in range(n):
    a = input("Enter the string: ")
    print(a[::-1])
    
