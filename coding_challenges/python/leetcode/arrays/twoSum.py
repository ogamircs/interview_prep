from itertools import permutations

def twoSumBruteForce(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    for i in range(0, n):
        for j in range(i+1, n):
            if(nums[i]+nums[j]==target):
                return [i, j]

def twoSumTwoPass(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    dict = {}
    for i in range(0, n):
        dict[nums[i]] = i

    for i in range(0, n):
        comp = target - nums[i]
        if(comp in dict and dict[comp]!=i):
            return [i, dict[comp]]

def twoSum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    dict = {}

    for i in range(0, n):
        comp = target - nums[i]
        if(comp in dict and dict[comp]!=i):
            return [i, dict[comp]]
        else:
            dict[nums[i]] = i

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    print(f"{nums}, {target} -> {twoSum(nums, target)}")

    nums = [3, 3]
    target = 6
    print(f"{nums}, {target} -> {twoSum(nums, target)}")

    nums = [2,5,5,11]
    target = 10
    print(f"{nums}, {target} -> {twoSum(nums, target)}")