
def findDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    dict = {}
    answer = []

    for i in range(len(nums)):
        if nums[i] in dict:
            dict[nums[i]] += 1
        else:
            dict[nums[i]] = 1

    for key, value in dict.items():
        if value > 1:
            answer.append(key)

    return answer

if __name__ == '__main__':
    solution = findDuplicates([4,3,2,7,8,2,3,1])
    print(solution)