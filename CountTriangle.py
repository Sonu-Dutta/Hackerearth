# You are given n triangles.
# You are required to find how many triangles are unique out of given triangles. For each triangle you are given three integers a,b,c , the sides of a triangle.
# A triangle is said to be unique if there is no other triangle with same set of sides.
# Note : It is always possible to form triangle with given sides.
# INPUT:
# First line contains n, the number of triangles. Each of next n lines contain three integers a,b,c (sides of a triangle).
# Output:
# print single integer, the number of unique triangles.
# Sample Input
# 5
# 7 6 5
# 5 7 6
# 8 2 9
# 2 3 4
# 2 4 3 
# Sample Output
# 1

n = int(input("Enter number of triangles: "))
l = []
for _ in range(n):
    a = tuple(map(int,input("Side of triangles: ").split()))
    a = sorted(a)
    
    l.append(tuple(a))
    print(l)
from collections import Counter

d = Counter(l)
print(d)
ans = 0
for k,v in d.items():
    if v ==1 :
        ans+=1
        
print(ans)