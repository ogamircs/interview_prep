class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        i = 0
        j = len(s)-1
        max = 0
        while(i<=j):
            dist_chars = len(set(s[i:(j+1)]))
            if(dist_chars>k):
                p = j
                while(j>i):
                    j -= 1
                    res1 = self.lengthOfLongestSubstringKDistinct(s[i:j+1], k)
                    if(res1>max):
                        max = res1
                j = p
                i = i+1
                res2 = self.lengthOfLongestSubstringKDistinct(s[i:j+1], k)
                if(res2>max):
                    max = res2
                #findSubStr(s, i, j-1, k)
            elif(dist_chars<=k):
                res3 = (j-i)+1
                if(res3>max):
                    max = res3
                return max
        return max
t = Solution()

s = "eceba"
k = 2
print(f"Answer is: {t.lengthOfLongestSubstringKDistinct(s,k)}")
#Explanation: The substring is "ece" with length 3.