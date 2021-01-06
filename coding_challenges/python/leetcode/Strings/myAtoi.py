from locale import atoi
import numpy as np

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    n = len(s)
    ans = i = j = 0
    neg = 1
    digits = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    INT_MAX = 2**31
    while i < n:
        if s[i] in digits:
            j = INT_MAX
            ans = ans * 10 + ord(s[i]) - ord('0')
        elif (j==i-1 or j==0) and s[i] == ' ':
            j = i
        elif (j==i-1 or j==0) and s[i] in {'+','-'}:
            j = INT_MAX
            if s[i]=='-':
                neg = -1
        else:
            break
        i += 1

    if ans*neg > INT_MAX - 1:
        return INT_MAX - 1
    elif ans*neg < -INT_MAX:
        return -INT_MAX
    else:
        return ans*neg

if __name__ == '__main__':
    s = "   1243"
    print(atoi(s))
    print(myAtoi(s))
    s = "   -42"
    print(myAtoi(s))
    s = "4193 with words"
    print(myAtoi(s))
    s = "words and 987"
    print(myAtoi(s))
    s = "-91283472332"
    print(myAtoi(s))
    s = "+-12"
    print(myAtoi(s))
    s = "00000-42a1234"
    print(myAtoi(s))
    s = "   +0 123"
    print(myAtoi(s))
