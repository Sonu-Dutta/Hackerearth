# String message will contain at least one digit, but not more than 100
# Each character in code will be a digit ('0'-'9').
# Sample Input
# 12134
# Sample Output
# 18

dic = [6,2,5,5,4,5,6,3,7,6]
s = str(input())
ct = 0
for i in s:
    ct+=dic[int(i)]
print(ct)