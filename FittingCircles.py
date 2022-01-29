# You are given a rectangle of length  and width . You are required to determine a circle that contains the maximum circumference that fits inside the rectangle. This type of circle is called a big circle. Your task is to determine the maximum number of big circles that can fit inside the rectangle. 

# Sample Input
# 1
# 40 10
# Sample Output
# 4
# Explanation
# 4 circles of radius 10 can fit inside the rectangle.
t =  int(input())
for i in range(t):
    a,b = map(int,input().split())
    if(a >= b):
        print(a//b)
    elif(a<b):
        print(b//a)