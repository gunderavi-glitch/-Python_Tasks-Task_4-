# problem 20 : No Idea!

# link : https://www.hackerrank.com/challenges/no-idea/problem

# code :

Read n and m
n, m = input().split()

# Read the array
array = input().split()

# Read sets A and B (converting them to sets for O(1) lookups)
A = set(input().split())
B = set(input().split())

# Calculate total happiness
happiness = sum((i in A) - (i in B) for i in array)

# Print the final happiness
print(happiness)
