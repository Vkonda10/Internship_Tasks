
# Problem: Pangrams
# HackerRank: https://www.hackerrank.com/challenges/pangrams/problem

def pangrams(s):
    letters = set(s.lower())
    return "pangram" if len(letters.intersection(set("abcdefghijklmnopqrstuvwxyz"))) == 26 else "not pangram"

if __name__ == '__main__':
    s = input()
    print(pangrams(s))
