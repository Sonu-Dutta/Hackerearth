# You are required to enter a word that consists of x and y that denote the number of Zs and Os respectively. 
# The input word is considered similar to word zoo if 2×x=y.

# Determine if the entered word is similar to word zoo.

# For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

# Sample Input
# zzzoooooo
# Sample Output
# Yes

t=int(input("Enter number of test cases: "))
for i in range(t):
    s=input("Enter string: ")
    li=[i for i in s]
    li1=[li[i] for i in range(len(li)) if li[i]=='z']
    li2=[li[i] for i in range(len(li)) if li[i]=='o']

    if (2*len(li1))==len(li2):
        print("Yes")
    else:
        print("No")
