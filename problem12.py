# Introduction to Sets
# link : https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

# code

def average(array):
    # your code goes here
    s = set(arr)
    return sum(s) / len(s)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
