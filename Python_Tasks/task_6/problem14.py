
# Problem: Set .intersection() Operation
# HackerRank: https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

if __name__ == '__main__':
    n = int(input())
    english_students = set(map(int, input().split()))

    b = int(input())
    french_students = set(map(int, input().split()))

    print(len(english_students.intersection(french_students)))
