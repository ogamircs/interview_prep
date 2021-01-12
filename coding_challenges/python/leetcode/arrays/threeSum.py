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

def threeSumN3(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []
    n = len(nums)
    nums.sort()
    for i in range(0, n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if(nums[i]+nums[j]+nums[k]==0):
                    new_set = [nums[i], nums[j], nums[k]]
                    new_set.sort()
                    if (not (new_set in ans)):
                        ans.append(new_set)

    return ans

def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ans = []
    n = len(nums)
    for i in range(0, n):
        target = 0 - nums[i]
        dict = {}
        for j in range(0,n):
            comp = target - nums[j]
            if ( (comp in dict) and (dict[comp]!=j) and (dict[comp]!=i) and (i!=j)):
                toAdd = [nums[i], nums[j], comp]
                toAdd.sort()
                if(not (toAdd in ans)):
                    ans.append(toAdd)
            else:
                dict[nums[j]] = j

    return ans


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    print(f"{nums} -> {threeSum(nums)}")
    #
    # nums = [-1,0,1,2,-1,-4]
    # print(f"{nums} -> {threeSum(nums)}")
    #
    # nums = []
    # print(f"{nums} -> {threeSum(nums)}")
    #
    nums = [0, 0]
    print(f"{nums} -> {threeSum(nums)}")