# Input:
# First line contains a string S, , where S denotes the length of the string.

# Output:
# Print an integer denoting the length of the longest good substring, that is substring consists of only vowels.

# SAMPLE INPUT 
# abcaac
# SAMPLE OUTPUT 
# 2
string = list(input())
vowels = ['a', 'e', 'i', 'o', 'u']
count = 0
ans = 0
for i in range(len(string)):
    if string[i] in vowels:
        count += 1
        ans = max(ans, count)
    else:
        count = 0
print(ans)