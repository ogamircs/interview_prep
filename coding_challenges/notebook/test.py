def validPalindrome(s):
    L = len(s)
    l = 0
    r = L-1
    skipped = False
    while(l<r):
        k = s[l]
        kk = s[r]
        if(s[l]==s[r]):
            l += 1
            r -= 1
        elif((not skipped) and (s[l]!=s[r])):
            skipped = True
            if(s[l+1]==s[r]):
                l += 1
            elif(s[l]==s[r-1]):
                r -= 1
            else:
                return False
        elif(skipped and (s[l]!=s[r])):
            return False
    return True

s = "aba"
s = "abbca"
#s = "abca"
#s = "abc"
#s = "abcf"
s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
print(validPalindrome(s))