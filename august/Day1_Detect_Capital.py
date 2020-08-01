'''
Given a word, you need to judge whether the usage of capitals in it is right or not.
We define the usage of capitals in a word to be right when one of the following cases holds:
    All letters in this word are capitals, like "USA".
    All letters in this word are not capitals, like "leetcode".
    Only the first letter in this word is capital, like "Google".

Otherwise, we define that this word doesn't use capitals in a right way.
'''

# Approach 1: Dictionary to count capitals
# Time Complexity: O(n)
# where n == len(word)
# Space Complexity: O(1)
#def detectCapitalUse(word):
#    """
#    :type word: str
#    :rtype: bool
#    """
#    dict = {}
#    cBig = 0
#    cSmall = 0
#
#    for i in range(len(word)):
#        if word[i] >= "A" and word[i] <= "Z":
#            cBig += 1
#            dict["big"] = cBig
#        else:
#            cSmall += 1
#            dict["small"] = cSmall

#    if word[0] >= "A" and word[0] <= "Z":
#        if dict["big"] == len(word):
#            return True
#        elif dict["small"] == len(word) - 1:
#            return True
#        else:
#            return False
#    elif word[0] >= "a" and word[0] <= "z":
#        if "big" in dict:
#            return False
#        else:
#            return True

# Approach 2: Character by Character with isupper()
# Time Complexity: O(n)
# where n == len(word), only need to check each char at most constant times
# Space Complexity: O(1)
# only need constant spaces to store variables
def detectCapitalUse(word):
    """
    :type word: str
    :rtype: bool
    """
    n = len(word)

    if len(word) == 1:
        return True

    # case 1: all capital
    if word[0].isupper() and word[1].isupper():
        for i in range(2,n):
            if not word[i].isupper():
                return False
    # case 2: not capitals & case 3: first capital
    else:
        for i in range(1,n):
            if word[i].isupper():
                return False

    # if pass all cases
    return True

if __name__ == '__main__':
    solution = detectCapitalUse("flaG")
    print(solution)
