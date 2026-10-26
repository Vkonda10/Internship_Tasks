
# Problem: Find the Runner-Up Score!
# HackerRank: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))

    unique_scores = sorted(set(scores), reverse=True)
    print(unique_scores[1])
