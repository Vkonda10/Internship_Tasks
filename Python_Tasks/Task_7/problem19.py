# Problem: Weighted Uniform Strings
# HackerRank: https://www.hackerrank.com/challenges/weighted-uniform-string/problem

def weightedUniformStrings(s, queries):
    weights = set()
    prev_char = ''
    count = 0

    for ch in s:
        if ch == prev_char:
            count += 1
        else:
            count = 1
            prev_char = ch

        weights.add((ord(ch) - ord('a') + 1) * count)

    return ['Yes' if q in weights else 'No' for q in queries]

if __name__ == '__main__':
    s = input().strip()
    n = int(input())
    queries = []

    for _ in range(n):
        queries.append(int(input()))

    result = weightedUniformStrings(s, queries)
    print('\n'.join(result))
