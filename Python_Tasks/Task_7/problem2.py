
# Problem: The Captain's Room
# HackerRank: https://www.hackerrank.com/challenges/py-the-captains-room/problem

if __name__ == '__main__':
    k = int(input())
    room_numbers = list(map(int, input().split()))

    unique_sum = sum(set(room_numbers))
    total_sum = sum(room_numbers)

    captain_room = (unique_sum * k - total_sum) // (k - 1)
    print(captain_room)
