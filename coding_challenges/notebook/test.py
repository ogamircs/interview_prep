def merge(nums1, m, nums2, n):
    i = 0
    j = 0
    num_zeroes = n

    if(n==0): 
        return None
    if(m==0): 
        for i in range(n):
            nums1[i] = nums2[i]
        return None

    while((num_zeroes>0) and (i<(m+n))):
        if((i==0) and (nums1[i]>nums2[j])):
            shiftForward(nums1, 1)
            nums1[i] = nums2[j]
            num_zeroes -= 1
            j += 1

        if((i>0) and (nums1[i]>nums2[j])):
            shiftForward(nums1, i+1)
            nums1[i] = nums2[j]
            num_zeroes -= 1
            j += 1
        i += 1
    
    if(num_zeroes>0):
        while((num_zeroes>0) and (i<(m+n))):
            nums1[i] = nums2[j]
            j += 1
            i + 1
            num_zeroes-=1
    return None

def shiftForward(nums, k):
    i = len(nums)-1
    while(i>=k):
        nums[i], nums[i-1] = nums[i-1], nums[i]
        i -= 1


nums1 = [-1,3,0,0,0,0,0]
m = 2
nums2 = [0,0,1,2,3]
n = 5
merge(nums1, m, nums2, n)
print(nums1)