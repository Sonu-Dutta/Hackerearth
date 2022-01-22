# You are conducting a contest at your college. This contest consists of two problems and  participants. You know the problem that a candidate will solve during the contest.

# You provide a balloon to a participant after he or she solves a problem. There are only green and purple-colored balloons available in a market. Each problem must have a balloon associated with it as a prize for solving that specific problem. You can distribute balloons to each participant by performing the following operation:

# Use green-colored balloons for the first problem and purple-colored balloons for the second problem
# Use purple-colored balloons for the first problem and green-colored balloons for the second problem
# You are given the cost of each balloon and problems that each participant solve. Your task is to print the minimum price that you have to pay while purchasing balloons.

# Input format

# First line:  that denotes the number of test cases ()
# For each test case: 
# First line: Cost of green and purple-colored balloons 
# Second line:  that denotes the number of participants ()
# Next  lines: Contain the status of users. For example, if the value of the  integer in the  row is , then it depicts that the  participant has not solved the  problem. Similarly, if the value of the  integer in the  row is , then it depicts that the  participant has solved the  problem.
# Output format
# For each test case, print the minimum cost that you have to pay to purchase balloons.

# Sample Input
# 2
# 9 6
# 10
# 1 1
# 1 1
# 0 1
# 0 0
# 0 1
# 0 0
# 0 1
# 0 1
# 1 1
# 0 0
# 1 9
# 10
# 0 1
# 0 0
# 0 0
# 0 1
# 1 0
# 0 1
# 0 1
# 0 0
# 0 1
# 0 0
# Sample Output
# 69
# 14

test_cases = int(input("Enter number of test cases: "))
for i in range(test_cases):
    p,g = map(int, input("Cost of Purple and Green balloons: ").split())
    n = int(input("Number of Participants: "))

    cost = 0
    lower = min(p,g)
    maximum = max(p,g)
    p1_total = 0
    p2_total = 0
    for i in range(n):
        p1,p2 = map(int, input("Status (solved or unsolved): ").split())
        p1_total += p1
        p2_total += p2

    if p1_total >= p2_total:
        cost += p1_total*lower
        cost += p2_total*maximum
    else:
        cost += p2_total*lower
        cost += p1_total*maximum
    print(cost)