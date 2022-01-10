
# You have been given 3 integers - l, r and k. Find how many numbers between l and r (both inclusive) are divisible by k. You do not need to print these numbers, you just have to find their count.

# Input Format
# The first and only line of input contains 3 space separated integers l, r and k.

# Output Format
# Print the required answer on a single line.

# Constraints

# Sample Input
# 1 10 1
# Sample Output
# 10

l,r,k = map(int,input("Enter numbers between l and r are divisible by k: ").split())
c=0
for i in range(l,r+1):
    if i%k==0:
        #print(i)
        c+=1
print(c)