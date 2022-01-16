# You are given an array A of length N. You need to find maximum length of subsequence of A which contains any one digit common in all the elements of that subsequence. 
# You are not allowed to count leading zeroes.
# Input Format:
# First line of input contains N, denoting number of elements.
# Second line of input contains N space separated integers, denoting array elements.
# Output Format:
# Single integer representing maximum length of subsequence containing one digit common.
# Sample Input
# 5
# 12 11 3 4 5
# Sample Output
# 2

# Explanation
# Maximum length subsequence with one digit common is [ 12 11 ].

a=int(input("Enter number of elements: "))
b=list(input("Enter elements: ").split())
max=0
for i in range(10):
    i=str(i)
    count=0
    for j in b:
        if(i in j):
            count=count+1
    if(count>max):
        max=count
print(max)