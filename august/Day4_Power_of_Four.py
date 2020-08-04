'''
Given an integer (signed 32 bits),
write a function to check whether it is a power of 4.
'''
# Approach 1: Divide by four
# Time Complexity: O(log n)
# Space Complexity: O(1)

def isPowerOfFour(num):
    """
    :type num: int
    :rtype: bool
    """
    # check 1
    if num == 1:
        return True

    powerOf = 4

    # check integer
    if num % powerOf != 0:
        return False

    # power of four is found
    if (num / powerOf) == 1 and (num % powerOf) == 0:
        return True
    elif (num / powerOf) < 1:
        return False
    else:
        next_number = num / powerOf
        return isPowerOfFour(next_number)

    return False

if __name__ == '__main__':
    # try 5, 1, 0
    solution = isPowerOfFour(16)
    print(solution)