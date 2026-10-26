# Task 3: Test all 15 functions from solutions.py

from solutions import (
    word_frequency, character_frequency, first_non_repeating,
    are_anagrams, first_repeating, move_zeros, second_highest,
    remove_duplicates, missing_number, two_sum_first, closest_to_zero,
    common_elements, rotate_right, max_consecutive_sum, all_pairs_sum
)

# Each question has the assignment example and one extra test.

print("Q1 example:", word_frequency("python is easy and python is powerful"))
print("Q1 extra:", word_frequency("Hi hi there"))

print("Q2 example:", character_frequency("banana"))
print("Q2 extra:", character_frequency("hello"))

print("Q3 example:", first_non_repeating("swiss"))
print("Q3 extra:", first_non_repeating("aabb"))

print("Q4 example:", are_anagrams("listen", "silent"))
print("Q4 extra:", are_anagrams("Dormitory", "dirty room"))

print("Q5 example:", first_repeating("programming"))
print("Q5 extra:", first_repeating("abcdef"))

print("Q6 example:", move_zeros([0, 3, 0, 1, 2, 0, 4]))
print("Q6 extra:", move_zeros([1, 0, 2, 0]))

print("Q7 example:", second_highest([10, 20, 40, 30, 40, 20]))
print("Q7 extra:", second_highest([5, 5, 5]))

print("Q8 example:", remove_duplicates([4, 2, 4, 5, 2, 7, 5]))
print("Q8 extra:", remove_duplicates(["a", "b", "a", "c"]))

print("Q9 example:", missing_number([1, 2, 4, 5, 6], 6))
print("Q9 extra:", missing_number([1, 3, 4], 4))

print("Q10 example:", two_sum_first([2, 7, 11, 15], 9))
print("Q10 extra:", two_sum_first([1, 4, 3, 6], 10))

print("Q11 example:", closest_to_zero([-8, -3, 2, 5, -2]))
print("Q11 extra:", closest_to_zero([-1, 1, 4]))

print("Q12 example:", common_elements([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
print("Q12 extra:", common_elements([3, 1, 3, 2], [2, 3, 3]))

print("Q13 example:", rotate_right([1, 2, 3, 4, 5], 2))
print("Q13 extra:", rotate_right([1, 2, 3], 5))

print("Q14 example:", max_consecutive_sum([4, 7, 2, 9, 5]))
print("Q14 extra:", max_consecutive_sum([-5, -2, -8]))

print("Q15 example:", all_pairs_sum([2, 4, 3, 5, 7, 8, 1], 9))
print("Q15 extra:", all_pairs_sum([1, 1, 2, 3, 4], 5))
