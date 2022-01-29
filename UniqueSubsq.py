# Sample Input
# 2
# 5
# ababa
# 5
# aaaac

# Sample Output
# 5
# 2

def result(str):
    count =0
    for i in range(len(str)-1):
        if str[i] != str[i+1]:
            count +=1
    return count+1
n = int(input())
for i in range(n):
    size = int(input())
    str = input()
    print(result(str))

