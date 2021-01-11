from itertools import permutations

def bfthreeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    perms = permutations(nums, 3)
    ans = []
    for p in perms:
        if(sum(p)==0):
            a = list(p)
            a.sort()
            if(not(a in ans)):
                ans.append(a)

    return ans

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    perms = permutations(nums, 3)
    ans = []
    for p in perms:
        if(sum(p)==0):
            a = list(p)
            a.sort()
            if(not(a in ans)):
                ans.append(a)
    return ans

if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(f"{nums} -> {threeSum(nums)}")

    nums = [-1,0,1,2,-1,-4, 1, -1, 3]
    print(f"{nums} -> {threeSum(nums)}")

    nums = []
    print(f"{nums} -> {threeSum(nums)}")

    nums = [0]
    print(f"{nums} -> {threeSum(nums)}")