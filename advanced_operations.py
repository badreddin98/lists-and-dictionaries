# Advanced Operations on Python Lists and Dictionaries
# By: [Your Name]
# Date: December 9, 2023

import time
import sys

# Lists Section
print("\n=== Lists Operations ===")

def create_squares_list(n):
    """
    Task 1: Create squares using list comprehension
    Time Complexity: O(n) - we iterate through n numbers once
    Space Complexity: O(n) - we store n squared numbers
    """
    squares = [num * num for num in range(1, n + 1)]
    return squares

# Testing Task 1
n = 5
result = create_squares_list(n)
print(f"\nTask 1 - Squares from 1 to {n}:")
print(f"Input: n = {n}")
print(f"Output: {result}")

def reverse_sublist(lst, i, j):
    """
    Task 2: Reverse a sublist within given indices
    Time Complexity: O(j-i) - we only reverse elements between i and j
    Space Complexity: O(1) - we modify the list in place
    """
    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i += 1
        j -= 1
    return lst

# Testing Task 2
test_list = [1, 2, 3, 4, 5, 6]
i, j = 1, 4
print(f"\nTask 2 - Reverse Sublist:")
print(f"Original list: {test_list}")
print(f"Reversing from index {i} to {j}")
result = reverse_sublist(test_list.copy(), i, j)
print(f"Result: {result}")

def merge_sorted_lists(list1, list2):
    """
    Task 3: Merge two sorted lists
    Time Complexity: O(n + m) where n and m are lengths of input lists
    Space Complexity: O(n + m) for the merged list
    """
    merged = []
    i = j = 0
    
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    
    # Add remaining elements
    merged.extend(list1[i:])
    merged.extend(list2[j:])
    return merged

# Testing Task 3
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print(f"\nTask 3 - Merge Sorted Lists:")
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Merged: {merge_sorted_lists(list1, list2)}")

# Dictionaries Section
print("\n=== Dictionary Operations ===")

def merge_dicts(dict1, dict2):
    """
    Task 1: Merge two dictionaries
    Time Complexity: O(n) where n is the total number of keys
    Space Complexity: O(n) for the new merged dictionary
    """
    merged = dict1.copy()
    merged.update(dict2)
    return merged

# Testing Dictionary Task 1
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print("\nDictionary Task 1 - Merge Dictionaries:")
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")
print(f"Merged: {merge_dicts(dict1, dict2)}")

def find_intersection(dict1, dict2):
    """
    Task 2: Find intersection of two dictionaries
    Time Complexity: O(min(n,m)) where n,m are sizes of dictionaries
    Space Complexity: O(min(n,m)) for storing common keys
    """
    return {k: dict1[k] for k in dict1 if k in dict2 and dict1[k] == dict2[k]}

# Testing Dictionary Task 2
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 2, 'c': 4, 'd': 5}
print("\nDictionary Task 2 - Find Intersection:")
print(f"Dict 1: {dict1}")
print(f"Dict 2: {dict2}")
print(f"Intersection: {find_intersection(dict1, dict2)}")

def word_frequency(words):
    """
    Task 3: Count word frequency
    Time Complexity: O(n) where n is number of words
    Space Complexity: O(k) where k is number of unique words
    """
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Testing Dictionary Task 3
word_list = ['apple', 'banana', 'apple', 'cherry', 'date', 'banana']
print("\nDictionary Task 3 - Word Frequency:")
print(f"Word List: {word_list}")
print(f"Frequency: {word_frequency(word_list)}")

# Performance Testing
print("\n=== Performance Testing ===")

# Testing list comprehension performance
start_time = time.time()
large_n = 10000
_ = create_squares_list(large_n)
print(f"\nTime taken for creating {large_n} squares: {time.time() - start_time:.4f} seconds")

# Testing dictionary operations performance
large_dict1 = {str(i): i for i in range(10000)}
large_dict2 = {str(i): i+1 for i in range(5000, 15000)}

start_time = time.time()
_ = merge_dicts(large_dict1, large_dict2)
print(f"Time taken for merging large dictionaries: {time.time() - start_time:.4f} seconds")
