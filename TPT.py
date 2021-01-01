# Two pointer technique implimentation

# Find the pair of elements in a sorted array (arr) that equal 15.

arr = [1, 3, 4, 6, 9, 14]
target = 15

# One way is to use the brute force solution which is to compare each element with every other number,
# but that's a time complexity of O(n^2) and there's a better option - two pointer technique.

# Two pointer creation

pointer_one = 0   # Points to first element in arr
pointer_two = len(arr) - 1   # Points to last element in arr

# This won't always be the case with this technique (sliding window concept pointers but have them move in a
# different direction). For our current purposes, it is more efficient to start wide, and iteratively narrow
# in (particularly if the array is sorted).


def two_sum(arr, target):
    pointer_one = 0
    pointer_two = len(arr) - 1

    while pointer_one < pointer_two:
        total = arr[pointer_one] + arr[pointer_two]
        if total == target:
            print(f"{arr[pointer_one]} + {arr[pointer_two]} = {total} ")
            break
        elif total < target:
            pointer_one += 1
        elif total > target:
            pointer_two -= 1


two_sum(arr, target)


# The time complexity of this solution is O(n) and space complexity is O(1),
# a significant improvement over the brute force technique.