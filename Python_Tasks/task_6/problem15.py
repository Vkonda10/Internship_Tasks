
# Problem: Set .difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english_students = set(map(int, input().split()))

    b = int(input())
    french_students = set(map(int, input().split()))

    print(len(english_students.difference(french_students)))
