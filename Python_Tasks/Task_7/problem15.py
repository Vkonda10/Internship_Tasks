# Problem: Game of Thrones - I
# HackerRank: https://www.hackerrank.com/challenges/game-of-thrones/problem

from collections import Counter

def gameOfThrones(s):
    freq = Counter(s)
    odd_count = sum(1 for count in freq.values() if count % 2 != 0)

    if odd_count <= 1:
        return "YES"
    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(gameOfThrones(s))
