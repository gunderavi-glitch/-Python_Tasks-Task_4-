# problem 13 : Symmetric Difference

# link : https://www.hackerrank.com/challenges/symmetric-difference/problem

# code

# Enter your code here. Read input from STDIN. Print output to STDOUT


m = int(input())
set_a = set(map(int, input().split()))
n = int(input())
set_b = set(map(int, input().split()))

symmetric_diff = set_a.symmetric_difference(set_b)

for item in sorted(symmetric_diff):
    print(item)
