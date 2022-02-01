# Sample Input
# 11
# babu
# anand
# rani
# aarti
# nandu
# rani
# rani
# ap
# anand
# babu
# nandu
# Sample Output
# 6
# aarti
# anand
# ap
# babu
# nandu
# rani

n = int(input())
l = []
for i in range(n):
    x = input()
    l.append(x)

l = list(set(l))
l.sort()
print(len(l))
for i in l:
    print(i)