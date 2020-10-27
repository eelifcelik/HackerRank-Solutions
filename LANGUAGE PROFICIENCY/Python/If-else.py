#Given an integer,n, perform the following conditional actions:

#If n is odd, print Weird
#If n is even and in the inclusive range of  to , print Not Weird
#If n is even and in the inclusive range of  to , print Weird
#If n is even and greater than , print Not Weird

# !/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input("n : ").strip())

    if (n % 2) == 1:
        print("Weird")

    else:
        if n in range(1, 5):
            print("Not Weird")

        if n in range(6, 21):
            print("Weird")

        if (n > 20):
            print("Not Weird")