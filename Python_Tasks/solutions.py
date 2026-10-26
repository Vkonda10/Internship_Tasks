# Task 3: Python Coding & Problem-Solving
# Each function returns its result so it can be reused in another file.

# Q1. Find the frequency of each word in a sentence
def word_frequency(sentence):
    counts = {}
    for word in sentence.split():
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts


# Q2. Find the frequency of each character in a word
def character_frequency(word):
    counts = {}
    for char in word:
        counts[char] = counts.get(char, 0) + 1
    return counts


# Q3. Find the first non-repeating character in a word
def first_non_repeating(word):
    counts = character_frequency(word)
    for char in word:
        if counts[char] == 1:
            return char
    return None


# Q4. Check whether two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1.replace(" ", "").lower()) == sorted(s2.replace(" ", "").lower())


# Q5. Find the first repeating character in a string
def first_repeating(string):
    seen = set()
    for char in string:
        if char in seen:
            return char
        seen.add(char)
    return None


# Q6. Move all zeros to the end of a list
def move_zeros(nums):
    non_zeros = [num for num in nums if num != 0]
    zeros = [num for num in nums if num == 0]
    return non_zeros + zeros


# Q7. Find the second highest distinct number in a list
def second_highest(nums):
    unique_nums = sorted(set(nums), reverse=True)
    if len(unique_nums) < 2:
        return None
    return unique_nums[1]


# Q8. Remove duplicates without changing the original order
def remove_duplicates(nums):
    result = []
    seen = set()
    for item in nums:
        if item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q9. Find the missing number from 1 to N
def missing_number(nums, n):
    return n * (n + 1) // 2 - sum(nums)


# Q10. Find the first pair whose sum equals a target
def two_sum_first(nums, target):
    seen = []
    for current in nums:
        needed = target - current
        for earlier in seen:
            if earlier == needed:
                return [earlier, current]
        seen.append(current)
    return []


# Q11. Find the number closest to zero (positive wins a tie)
def closest_to_zero(nums):
    return min(nums, key=lambda num: (abs(num), num < 0))


# Q12. Find common elements, preserving first-list order
def common_elements(list1, list2):
    second_set = set(list2)
    result = []
    seen = set()
    for item in list1:
        if item in second_set and item not in seen:
            result.append(item)
            seen.add(item)
    return result


# Q13. Rotate a list to the right by K positions
def rotate_right(nums, k):
    if not nums:
        return []
    k = k % len(nums)
    if k == 0:
        return nums.copy()
    return nums[-k:] + nums[:-k]


# Q14. Find the maximum sum of two consecutive elements
def max_consecutive_sum(nums):
    return max(nums[i] + nums[i + 1] for i in range(len(nums) - 1))


# Q15. Find all unique pairs that add up to a target
def all_pairs_sum(nums, target):
    pairs = set()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pairs.add(tuple(sorted((nums[i], nums[j]))))
    return [list(pair) for pair in sorted(pairs)]
