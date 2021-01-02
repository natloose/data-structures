# Binary Search Implimentation

# Binary Search is a naturally recursive algorithm, since the same process is repeated on smaller and smaller
# arrays until an array of size 1 has been found. However, there is of course an iterative implementation as well.

# Iterative
# The iterative approach is very simple and similar to the recursive approach. Here, we just perform the checks
# in a while loop:

arr = [1, 2, 3, 4, 7, 10, 15, 20, 28, 29, 35, 55, 89, 109]
element = 3


def binary_search_recursive(arr, element):

    start = 0
    mid = 0
    end = len(arr)
    step = 0

    while start <= end:

        print("Subarray in step {}: {}".format(step, str(arr[start:end + 1])))
        step = step + 1
        mid = (start + end) // 2

        if element == arr[mid]:
            print(f"Number 3 is located at index {mid}.")
            break
        elif element < arr[mid]:
            end = mid - 1
        elif element > arr[mid]:
            start = mid + 1


binary_search_recursive(arr, element)