# You are given an array A of size N that contains integers. Here,  is an even number. 
# You are required to perform the following operations:

# Divide the array of numbers in two equal halves
# Note: Here, two equal parts of a test case are created by dividing the array into two equal parts.
# Take the first digit of the numbers that are available in the first half of the array (first 50% of the test case)
# Take the last digit of the numbers that are available in the second half of the array (second 50% of the test case)
# Generate a number by using the digits that have been selected in the above steps
# Your task is to determine whether the newly-generated number is divisible by .

# Sample Input
# 6
# 15478 8452 8232 874 985 4512
# Sample Output
# OUI

# Explanation
# The first digit of 15478 is 1.
# The first digit of 8452 is 8.
# The first digit of 8232 is 8.
# The last digit of 874 is 4.
# The last digit of 985 is 5.
# The last digit of 4512 is 2.
# The newly generated number will be 188452 which is divisible by 11.

n = int(input("Enter the size of the array: "))
s = list(input("Enter array elements: ").split())

half = n/2
x = []
for i in range(n):
    if i < half:
        x.append(s[i][0])
    else:
        x.append(s[i][-1:])

temp = ''.join(x)

if (int(temp) % 11 == 0):
    print("OUI")
else:
    print("NON")