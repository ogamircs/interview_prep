from collections import Counter
def minWindow(s: str, t: str) -> str:
    m = len(s)
    n = len(t)
    if(n>m):
        return ""
    if(s==t): 
        return t
    c = Counter(t)
    l=0
    r=0
    res = dict()
    while(l<m):
        if(r>=m):
            c = Counter(t)
            l += 1
            r = l
            continue
        test = s[r]
        if(s[r] in c):
            if(c[s[r]]>0):
                c[s[r]] -= 1
            else:
                c = Counter(t)
                l += 1
                r = l
                continue

        if(len(list(c.elements())) == 0):
            #reached a diserable state
            res[r-l+1]=(tuple([l,r]))
            c = Counter(t)
            l += 1
            r = l-1
        r += 1

    if(len(res)==0): return ""
    output = res[min(list(res.keys()))]
    return s[output[0]:output[1]+1],output,res

s = "EBANC"
t = "ABC"
print(minWindow(s,t))