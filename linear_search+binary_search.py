# Romain Tranchant
# CIS103 - Homework Assignment 5
# Instructor : MD Ali
# Topic: Searching, Sorting, and Complexity Analysis

# Problem 1: Implementing Linear Search and Binary Search

# 1. **Linear Search**: Implement a function that performs linear search. The function should
# take a list and a target element as input and return the index of the target element if found,
# otherwise return `-1`.
# 2. **Binary Search**: Implement a function that performs binary search on a sorted list. The
# function should return the index of the target element if found, otherwise return `-1`.
# - **Hint**: Remember that binary search requires the list to be sorted in advance.
# 3. **Comparing Time Complexity**: Write a Python program that compares the performance of
# both algorithms on lists of varying sizes (e.g., 1000, 10,000, and 100,000 elements). Use Python’s
# `time` module to measure the time taken by each algorithm.

# **Code Requirements:**
# - Implement both `linear_search()` and `binary_search()` functions.
# - Write a driver code that tests both search algorithms on the same data sets and prints out the
# time taken for each.


# Imports the time module, which allows us to measure how long search operations take.
import time

# Defines a function linearsearch that searches for a target in a list using linear search.
def linearsearch(lyst, target):
# Initializes the position index to zero.
    position = 0
# Loops through the list until the end is reached.
    while position < len(lyst):
# Checks if the current element matches the target.
        if target == lyst[position]:
# Returns the position if the target is found.
            return position
# Increments the position to check the next element.
        position += 1
# Returns -1 if the target is not found in the list.
    return -1

# Defines a function binarySearch that searches for a target in a sorted list using binary search.
def binarySearch(lyst, target):
# Initializes the left pointer to the start of the list.
    left = 0
# Initializes the right pointer to the end of the list.
    right = len(lyst) - 1
# Loops until the left pointer exceeds the right pointer.
    while left <= right:
# Calculates the midpoint index of the current search range.
        midpoint = (left + right) // 2
# Checks if the target matches the midpoint element.
        if target == lyst[midpoint]:
# Returns the midpoint index if the target is found.
            return midpoint
# If the target is less than the midpoint element, adjusts the right pointer.
        elif target < lyst[midpoint]:
            right = midpoint - 1
        else:
# If the target is greater than the midpoint element, adjusts the left pointer.
            left = midpoint + 1
# Returns -1 if the target is not found in the list.
    return -1

# Sets the target value for the search and creates a list of numbers from 0 to 999.
target = 999
lyst = range(1000)
# Records the start time for linear search.
start_time = time.time()
# Calls the linearsearch function to find the target in the list.
result = linearsearch(lyst, target)
# Records the end time after searching.
end_time = time.time()
# Calculates the total time taken for the linear search.
elapsed = end_time - start_time
# Prints the elapsed time for the linear search operation.
print(f"Linear search of {target} in {len(lyst)} lasted {elapsed:.9f} seconds.")

# Records the start time for binary search.
start_time = time.time()
# Calls the binarySearch function to find the target in the list.
result = binarySearch(lyst, target)
# Records the end time after searching.
end_time = time.time()
# Calculates the total time taken for the binary search.
elapsed_binary = end_time - start_time
# Prints the elapsed time for the binary search operation.
print(f"Binary search of {target} in {len(lyst)} lasted {elapsed_binary:.9f} seconds.")

# Sets a new target value for the search and creates a list of numbers from 0 to 9999.
target = 9999
lyst = range(10000)
# Records the start time for the new linear search.
start_time = time.time()
result = linearsearch(lyst, target)
end_time = time.time()
elapsed = end_time - start_time
print(f"Linear search of {target} in {len(lyst)} lasted {elapsed:.9f} seconds.")

# Records the start time for the new binary search.
start_time = time.time()
result = binarySearch(lyst, target)
end_time = time.time()
elapsed_binary = end_time - start_time
print(f"Binary search of {target} in {len(lyst)} lasted {elapsed_binary:.9f} seconds.")

# Sets a new target value for the search and creates a list of numbers from 0 to 99999.
target = 99999
lyst = range(100000)
# Records the start time for the new linear search.
start_time = time.time()
result = linearsearch(lyst, target)
end_time = time.time()
elapsed = end_time - start_time
print(f"Linear search of {target} in {len(lyst)} lasted {elapsed:.9f} seconds.")


# Records the start time for the new binary search.
start_time = time.time()
result = binarySearch(lyst, target)
end_time = time.time()
elapsed_binary = end_time - start_time
print(f"Binary search of {target} in {len(lyst)} lasted {elapsed_binary:.9f} seconds.")
