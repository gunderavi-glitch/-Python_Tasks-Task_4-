# problem 14 : Set .add()
# link : https://www.hackerrank.com/challenges/symmetric-difference/problem

# code


n = int(input())


stamps = set()

for _ in range(n):
    stamps.add(input().strip())

print(len(stamps))
