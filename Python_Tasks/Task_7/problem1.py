
# Problem: Set .symmetric_difference() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem

if __name__ == '__main__':
    n = int(input())
    english_students = set(map(int, input().split()))

    b = int(input())
    french_students = set(map(int, input().split()))

    result = english_students.symmetric_difference(french_students)
    print(len(result))
