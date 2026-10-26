
# Problem: Alphabet Rangoli
# HackerRank: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string

def print_rangoli(size):
    alphabet = string.ascii_lowercase
    width = 4 * size - 3

    for i in range(size - 1, -size, -1):
        row = (
            alphabet[size - 1:abs(i):-1]
            + alphabet[abs(i):size]
        )
        print("-".join(row).center(width, "-"))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
