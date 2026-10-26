# Problem: Anagram
# HackerRank: https://www.hackerrank.com/challenges/anagram/problem

from collections import Counter

def anagram(s):
    n = len(s)

    if n % 2 != 0:
        return -1

    first = s[:n // 2]
    second = s[n // 2:]

    count1 = Counter(first)
    count2 = Counter(second)

    return sum((count1 - count2).values())

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(anagram(s))
