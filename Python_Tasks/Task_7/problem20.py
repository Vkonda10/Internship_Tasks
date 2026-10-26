# Problem: Super Reduced String
# HackerRank: https://www.hackerrank.com/challenges/reduced-string/problem

def superReducedString(s):
    stack = []

    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)

    return ''.join(stack) if stack else "Empty String"

if __name__ == '__main__':
    s = input().strip()
    print(superReducedString(s))
