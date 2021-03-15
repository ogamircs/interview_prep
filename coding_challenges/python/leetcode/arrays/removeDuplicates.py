def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    element = None
    l = len(nums)
    for i in range(0,l):
        if(element != nums[i]):
            element = nums[i]
        elif(element == nums[i]):



    return len(nums)

if __name__ == '__main__':
    nums = [1,1,2]
    l = removeDuplicates(nums)
    print(f"{l}, nums = {nums}")



