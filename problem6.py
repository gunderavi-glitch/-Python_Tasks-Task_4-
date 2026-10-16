# problem 6 : Find the Runner-Up Score!

# Hacker rank link : https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

# code
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    u_c = set(arr)
    s_s = sorted(u_c, reverse = True)
    print(s_s[1])
