# problem 1 : Python If-Else
#  Hacker rank link ": https://www.hackerrank.com/challenges/py-if-else/problem


#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())
   # If n is odd
    if n % 2 != 0:
        print("Weird")
    # If n is even
    else:
        if 2 <= n <= 5:
            print("Not Weird")
        elif 6 <= n <= 20:
            print("Weird")
        elif n > 20:
            print("Not Weird")
        

        
