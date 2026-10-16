# problem 7 : String Split and Join
# link : https://www.hackerrank.com/challenges/python-string-split-and-join/problem

# code

def split_and_join(line):
    # write your code here
    return "-".join(line.split(" "))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
