
# Problem: Funny String
# HackerRank: https://www.hackerrank.com/challenges/funny-string/problem

def funnyString(s):
    original = [ord(s[i]) for i in range(len(s))]
    reversed_s = s[::-1]
    reversed_codes = [ord(reversed_s[i]) for i in range(len(reversed_s))]

    for i in range(1, len(s)):
        if abs(original[i] - original[i - 1]) != abs(reversed_codes[i] - reversed_codes[i - 1]):
            return "Not Funny"

    return "Funny"

if __name__ == '__main__':
    q = int(input())
    for _ in range(q):
        s = input().strip()
        print(funnyString(s))
