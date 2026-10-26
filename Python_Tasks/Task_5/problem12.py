
# Problem: Capitalize!
# HackerRank: https://www.hackerrank.com/challenges/capitalize/problem

import os

def solve(s):
    return ' '.join(word.capitalize() for word in s.split(' '))

if __name__ == '__main__':
    s = input()
    result = solve(s)

    with open(os.environ['OUTPUT_PATH'], 'w') as f:
        f.write(result + '\n')
