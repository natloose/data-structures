arr = [1, 2, 6, 10, 13, 19]
k = 3


def length_of_longest_substring(arr, k):
    # Define max sum variable which we'll initialize to -infinity
    max_sum = float('-inf')
    # Define start pointer which will be the beginning of our sliding window
    start = 0
    # Sum of all the values inside our sliding window
    current_sum = 0

    for end, val in enumerate(arr):
        current_sum += val
        # Create sliding window of size k
        if end - start + 1 == k:
            # Check if sum inside window is > max_sum
            max_sum = max(max_sum, current_sum)
            # Advance sliding window without increase window size of k
            # Subtract start value from current_sum
            current_sum -= arr[start]
            # Advance start by 1
            start += 1
    return max_sum




length_of_longest_substring(arr, k)



