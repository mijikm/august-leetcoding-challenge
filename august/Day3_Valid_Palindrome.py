# Approach 1: Char by char
# Time Complexity: O(n)
# Space Complexity: O(1)

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    answer = ""
    for i in range(len(s)):
        if (s[i] >= "a" and s[i] <= "z") or (s[i] >= "A" and s[i] <= "Z") or (s[i] >= "0" and s[i] <= "9"):
            answer += ''.join(s[i])

    if answer.lower() == answer[::-1].lower():
        return True
    else:
        return False

if __name__ == '__main__':
    # try "A man, a plan, a canal: Panama", "09"
    solution = isPalindrome("race a car")
    print(solution)