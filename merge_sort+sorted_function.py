# Romain Tranchant
# CIS103 - Homework Assignment 5
# Instructor : MD Ali
# Topic: Searching, Sorting, and Complexity Analysis

# Problem 4: Analyzing Python’s Built-in Sorting Algorithm

# Python’s built-in `sort()` method and `sorted()` function use a highly optimized sorting algorithm
# called **Timsort**, which is a hybrid sorting algorithm derived from merge sort and insertion
# sort.
# 1. Use Python’s `sorted()` function to sort a list of integers.
# 2. Measure the performance of `sorted()` and compare it with your implementation of merge
# sort.


# Imports the time module, which allows us to measure how long sorting operations take.
import time

# Defines a function merge that merges two sorted sublists of the_list2.
def merge(the_list2, copyBuffer, low, middle, high):
# Initializes i1 and i2 to the first items in each sublist.
    i1 = low
    i2 = middle + 1
# Interleaves items from the sublists into the copyBuffer.
    for i in range(low, high + 1):
# Checks if the first sublist is exhausted.
        if i1 > middle:  # First sublist exhausted
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

# Creates a sample list to be sorted, in descending order.
the_list2 = list(range(1000000)[::-1])
# Prints the number of items in the unsorted list.
print(f"The unsorted list has {len(the_list2)} items")
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

# Creates another sample list to test the built-in sorted function, in descending order.
the_list2 = list(range(1000000)[::-1])
# Records the start time for the built-in sorted function.
start_sorted = time.time()
# Calls the sorted function to sort the list.
sorted_list = sorted(the_list2)
# Records the end time after sorting.
end_sorted = time.time()
# Calculates the total time taken for the sorted function.
elapsed_sort = end_sorted - start_sorted
# Prints the elapsed time for the sorted function.
print(f"Sorted function lasted {elapsed_sort:.9f} seconds.")