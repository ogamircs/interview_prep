def numberOfWays(arr,k):
    n = len(arr)
    res = 0
    i = 0
    j = n-1
    a = sorted(arr)
    while(i<j):
        if((a[i]+a[j])==k):
            if(a[i]==a[j]):
                count = j - i + 1
                res += (count * (count - 1)) // 2
                break
            else:
                # Count duplicates for a[i] and a[j]
                left_count = 1
                right_count = 1
                while i + 1 < j and a[i] == a[i + 1]:
                    left_count += 1
                    i += 1
                while j - 1 > i and a[j] == a[j - 1]:
                    right_count += 1
                    j -= 1
            res += left_count * right_count  # Total pairs for current i and j
            i += 1
            j -= 1
        elif((a[i]+a[j])>k):
            j -= 1
        else:
            i += 1
        
    return res

arr = [1, 5, 3, 3, 3]
arr = [1, 3, 3, 3, 5]
k = 6
print(numberOfWays(arr,k))