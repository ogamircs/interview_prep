def lengthOfLongestSubstringBad(s):
    """
    :type s: str
    :rtype: int
    """
    sarr = list(s)
    max_lss = 0

    for start_pos in range(0, len(sarr)):
        lss = [sarr[start_pos]]
        k = 0
        for i in range(start_pos+1, len(sarr)):
           if (not (sarr[i] in lss)) and (sarr[i-1]==lss[k]):
               k += 1
               lss.append(sarr[i])
           elif((sarr[i] in lss)):
               break
        print(lss)
        if( len(lss)>max_lss):
            max_lss = len(lss)
    return max_lss



def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    ans = i = j = 0
    n = len(s)
    lss = set()

    while (i < n and j < n):
        if not (s[j] in lss):
            lss.add(s[j])
            j += 1
            ans = max(ans, j - i)
        else:
            lss.remove(s[i])
            i += 1
    return ans


if __name__ == '__main__':
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
    s = "bbbbb"
    print(lengthOfLongestSubstring(s))
    s = "pwwkew"
    print(lengthOfLongestSubstring(s))
    s = ""
    print(lengthOfLongestSubstring(s))