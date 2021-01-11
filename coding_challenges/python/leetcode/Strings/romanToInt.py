def romanToInt(s):
    """
    :type s: str
    :rtype: int
    """
    symbol_map = { "I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000 }
    ans = 0
    n = len(s)
    for i in range(0, n):
        ans = ans + symbol_map[s[i]]

        if(i<n-1 and symbol_map[s[i+1]]>symbol_map[s[i]]):
            ans = ans - symbol_map[s[i]]*2
    return ans

if __name__ == '__main__':
    s = "III"
    print(f"{s} - {romanToInt(s)}")

    s = "XII"
    print(f"{s} - {romanToInt(s)}")

    s = "IV"
    print(f"{s} - {romanToInt(s)}")

    s = "IX"
    print(f"{s} - {romanToInt(s)}")

    s = "LVIII"
    print(f"{s} - {romanToInt(s)}")

    s = "MCMXCIV"
    print(f"{s} - {romanToInt(s)}")