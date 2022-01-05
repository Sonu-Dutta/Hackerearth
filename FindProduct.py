# You have been given an array A of size N consisting of positive integers.
# You need to find and print the product of all the number in this array Modulo 10**9 + 7
arr = input("Enter elements: ")
num = input("Enter size: ")

answer = 1
for item in arr.split():
    answer = (answer * int(item)) % (10**9 + 7)
print(answer)