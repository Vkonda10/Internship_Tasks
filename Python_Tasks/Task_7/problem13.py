# Problem: Sherlock and the Valid String
# HackerRank: https://www.hackerrank.com/challenges/sherlock-and-the-valid-string/problem




def isValid(s):
    freq = Counter(Counter(s).values())

    if len(freq) == 1:
        return "YES"

    if len(freq) == 2:
        keys = list(freq.keys())

        if (keys[0] == 1 and freq[keys[0]] == 1) or \
           (keys[1] == 1 and freq[keys[1]] == 1):
            return "YES"

        if abs(keys[0] - keys[1]) == 1:
            larger = max(keys)
            if freq[larger] == 1:
                return "YES"

    return "NO"

if __name__ == '__main__':
    s = input().strip()
    print(isValid(s))
