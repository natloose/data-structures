# Practice Questions

# Binary Search

# Q1. Return index of element using an iterative approach
arr = [1, 2, 5, 9, 10, 19, 20, 28, 29, 35]
element = 35


def binary_search_iterative(arr, element):
    start = 0
    mid = 0
    end = len(arr)

    while start <= end:
        mid = (start + end) // 2

        if element == arr[mid]:
            print(mid)
            break
        elif element < arr[mid]:
            end = mid - 1
        elif element > arr[mid]:
            start = mid + 1


# binary_search_iterative(arr, element)



# Q2. Return index of k using recursive approach
arr = [1, 2, 5, 9, 10, 19, 20, 28, 29, 35]
k = 19

# Two-Pointer

# Q1. Find the pair of elements in a sorted array (a) that equal 30.
a = [2, 3, 8, 14, 19, 22, 25, 26]
targ = 30


def tpt(a, targ):
    pointer_one = 0
    pointer_two = len(a) - 1

    while pointer_one < pointer_two:
        total = a[pointer_one] + a[pointer_two]
        if total == targ:
            print(pointer_one, pointer_two)
            break
        elif total < targ:
            pointer_one += 1
        elif total > targ:
            pointer_two -= 1

tpt(a, targ)






# Sliding-Window

# Q1. Find the maximum k-sized subarray value from the contiguous array
ar = [1, 2, 6, 10, 13, 19]
k = 3


def sliding_window(ar, size):
    start = 0
    current_sum = 0
    max_sum = float('-inf')

    for end, val in enumerate(ar):
        current_sum += val
        if end - start + 1 == k:
            max_sum = max(max_sum, current_sum)
            current_sum -= arr[start]
            start += 1
    print(max_sum)

sliding_window(ar, k)









