# problem 19 : Collections.Counter()

# link : https://www.hackerrank.com/challenges/collections-counter/problem

# code :

from collections import Counter

# Read the number of shoes
num_shoes = int(input())

# Read the available shoe sizes and count them
shoe_sizes = Counter(map(int, input().split()))

# Read the number of customers
num_customers = int(input())

total_money = 0

# Process each customer's request
for _ in range(num_customers):
    size, price = map(int, input().split())
    # If the requested shoe size is available
    if shoe_sizes[size] > 0:
        total_money += price
        shoe_sizes[size] -= 1  # Decrease the inventory for that size

# Print the total money earned
print(total_money)
