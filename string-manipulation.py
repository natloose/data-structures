# Given an integer, return the integer with reversed digits.
# Note: The integer could be either positive or negative.

#  Q1. Reverse Integer (string manipulation allowed)

def reverse(x):
    # Convert to int if not already
    x = int(x)
    # If number is a negative remove it (to be replaced later)
    minus = -1 if x < 0 else 1
    x *= minus

    # Convert to String
    x = str(x)
    # Reverse
    x = ''.join(reversed(x))
    # Re-add minus if applicable
    x = int(x) * minus

    return x


reverse(int(-1000099))

# Q2. Reverse Interger without converting to string


def reverse_int(x):
    x = int(x)
    minus = -1 if x < 0 else 1
    x *= minus
    reverse = 0

    while x > 0:
        remainder = x % 10
        reverse = (reverse * 10) + remainder
        x = x // 10

    print(reverse*minus)


reverse_int(-109101)








