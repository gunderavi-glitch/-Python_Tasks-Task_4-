# problem 18 : Lists

# link : https://www.hackerrank.com/challenges/python-lists/problem

# code:
if __name__ == '__main__':
    n = []

    n.insert(0, 5)
    n.insert(1, 10)
    n.insert(0, 6)
    print(n)

    n.remove(6)
    n.append(9)
    n.append(1)
    n.sort()
    print(n)

    n.pop()
    n.reverse()
    print(n)
