# Vowels are very essential characters to form any meaningful word in English dictionary. 
# There are 5 vowels in English language - a, e, i, o u. You are given a randoms string containing only lowercase letters and you need to find if the string contains ALL the vowels.

# Sample Input
# 8
# atuongih
# Sample Output
# NO

n = int(input("Enter size of the string: "))
s = input("Enter the letters: ")
a = 0
e=0
i=0
o=0
u=0
for j in range(n):
    if s[j]=='a':
        a+=1
    if s[j]=='e':
        e+=1
    if s[j]=='i':
        i+=1
    if s[j]=='o':
        o+=1
    if s[j]=='u':
        u+=1
        
if a>0 and e>0 and i>0 and o>0 and u>0:
    print("YES")
else:
    print("NO")
        