# Romain Tranchant
# CIS103 - Homework Assignment 5
# Instructor : MD Ali
# Topic: Searching, Sorting, and Complexity Analysis

# Problem 2: Implementing Sorting Algorithms

# 1. **Bubble Sort**: Implement the bubble sort algorithm in Python. Your function should take
# an unsorted list and return the list sorted in ascending order.

# 2. **Merge Sort**: Implement the merge sort algorithm in Python. Your function should
# recursively divide the list, sort it, and then merge the sorted sublists.

# 3. **Comparing Time Complexity**: Test both sorting algorithms on lists of varying sizes (e.g.,
# 1000, 10,000, and 100,000 elements) and use Python’s `time` module to compare their
# performance.

# **Code Requirements:**
# Implement both `bubble_sort()` and `merge_sort()` functions.
# Write a driver code that tests both sorting algorithms on the same data sets and prints out the
# time taken for each.




# Imports the time module, which allows us to measure how long sorting operations take.
import time

# Defines a function bubble_sort that takes a single argument the_list2, which is the list to be
# sorted using the bubble sort algorithm.
def bubble_sort(the_list2):
# Starts an outer loop that iterates from the end of the list down to the first element.
    for n in range(len(the_list2) - 1, 0, -1):
# Initializes swapped for each pass.
        swapped = False
# Inner loop to compare adjacent elements.
        for i in range(n):
# Checks if the current element is greater than the next element.
            if the_list2[i] > the_list2[i + 1]:
# Swaps elements if they are in the wrong order.
                the_list2[i], the_list2[i + 1] = the_list2[i + 1], the_list2[i]
# Sets swapped to True, indicating that a swap has occurred.
                swapped = True
# If no elements were swapped during the inner loop, the list is sorted, and the outer loop can exit early.
        if not swapped:
            break
# Returns the sorted list.
    return the_list2

# Defines a function merge that merges two sorted sublists of the_list2.
def merge(the_list2, copyBuffer, low, middle, high):
# Initializes i1 and i2 to the first items in each sublist.
    i1 = low
    i2 = middle + 1
# Interleaves items from the sublists into the copyBuffer.
    for i in range(low, high + 1):
# Checks if the first sublist is exhausted.
        if i1 > middle:
# Copies the next element from the second sublist to the buffer.
            copyBuffer[i] = the_list2[i2]
            i2 += 1
# Checks if the second sublist is exhausted.
        elif i2 > high:
# Copies the next element from the first sublist to the buffer.
            copyBuffer[i] = the_list2[i1]
            i1 += 1
# Compares items from both sublists.
        elif the_list2[i1] < the_list2[i2]:
# If the element from the first sublist is smaller, it is copied to the buffer.
            copyBuffer[i] = the_list2[i1]
            i1 += 1
        else:
# If the element from the second sublist is smaller, it is copied to the buffer.
            copyBuffer[i] = the_list2[i2]
            i2 += 1
# Copies sorted items back to the proper position in the original list.
    for i in range(low, high + 1):
        the_list2[i] = copyBuffer[i]

# Defines a function merge_sort that sorts the list using the merge sort algorithm.
def merge_sort(the_list2, copyBuffer, low, high):
# Checks if the segment contains more than one element.
    if low < high:
# Calculates the middle index to divide the list into two halves.
        middle = (low + high) // 2
# Recursively sorts the left half.
        merge_sort(the_list2, copyBuffer, low, middle)
# Recursively sorts the right half.
        merge_sort(the_list2, copyBuffer, middle + 1, high)
# Merges the sorted halves.
        merge(the_list2, copyBuffer, low, middle, high)

# Sample list to be sorted using bubble sort.
the_list2 = list(range(1000)[::-1])
# Prints the number of items in the unsorted list.
print(f"The unsorted list has {len(the_list2)} items")
# Records the start time for bubble sort.
start_test = time.time()
# Calls the bubble_sort function to sort the list.
sorted_bubble = bubble_sort(the_list2)
# Records the end time after sorting.
end_time = time.time()
# Calculates the total time taken for the bubble sort.
elapsed_time = end_time - start_test
# Prints the elapsed time for the bubble sort operation.
print(f"Bubble sort lasted {elapsed_time:.9f} seconds.")
# Outputs the sorted list.
print(the_list2)

# Sample list to be sorted using merge sort.
the_list2 = list(range(1000)[::-1])
# Creates a buffer for merging.
copyBuffer = [0] * len(the_list2)
# Records the start time for merge sort.
start_test = time.time()
# Calls the merge_sort function to sort the list.
merge_sort(the_list2, copyBuffer, 0, len(the_list2) - 1)
# Records the end time after sorting.
end_time = time.time()
# Calculates the total time taken for the merge sort.
elapsed_time = end_time - start_test
# Prints the elapsed time for the merge sort operation.
print(f"Merge sort lasted {elapsed_time:.9f} seconds.")
# Outputs the sorted list.
print(the_list2)

# Updated sample list to be sorted using bubble sort
the_list2 = list(range(10000)[::-1])
print(f"The unsorted list has {len(the_list2)} items")
start_test = time.time()
sorted_bubble = bubble_sort(the_list2)
end_time = time.time()
elapsed_time = end_time - start_test
print(f"Bubble sort lasted {elapsed_time:.9f} seconds.")
print(the_list2)

# Updated sample list to be sorted using merge sort.
the_list2 = list(range(10000)[::-1])
copyBuffer = [0] * len(the_list2)
start_test = time.time()
merge_sort(the_list2, copyBuffer, 0, len(the_list2) - 1)
end_time = time.time()
elapsed_time = end_time - start_test
print(f"Merge sort lasted {elapsed_time:.9f} seconds.")
print(the_list2)

# Updated sample list to be sorted using merge sort.
the_list2 = list(range(100000)[::-1])
print(f"The unsorted list has {len(the_list2)} items")
copyBuffer = [0] * len(the_list2)
start_test = time.time()
merge_sort(the_list2, copyBuffer, 0, len(the_list2) - 1)
end_time = time.time()
elapsed_time = end_time - start_test
print(f"Merge sort lasted {elapsed_time:.9f} seconds.")
print(the_list2)

# Updated sample list to be sorted using bubble sort.
the_list2 = list(range(100000)[::-1])
start_test = time.time()
sorted_bubble = bubble_sort(the_list2)
end_time = time.time()
elapsed_time = end_time - start_test
print(f"Bubble sort lasted {elapsed_time:.9f} seconds.")
print(the_list2)

