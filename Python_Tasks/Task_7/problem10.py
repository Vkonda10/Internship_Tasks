# Problem: CamelCase
# HackerRank: https://www.hackerrank.com/challenges/camelcase/problem

def camelcase(s):
    return 1 + sum(1 for ch in s if ch.isupper())

if __name__ == '__main__':
    s = input().strip()
    print(camelcase(s))
