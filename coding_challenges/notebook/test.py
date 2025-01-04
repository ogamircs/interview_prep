def spiralArray(n):
    def spiral(a):
        n = len(a)
        r = c = 0
        for i in range(n*n):
            a[r][c] = i+1

            if(i+1<n):
                c+=1
            elif(i+1<(n*2)-1):
                r+=1
            elif(i+1<(n*3)-2):
                c-=1
            elif(i+1<(n*4)-4):
                r-=1
            else:
                break
            
    arr = []
    for i in range(n):
        sarr = []
        for j in range(n):
            sarr.append(0)
        arr.append(sarr)
    
    spiral(arr)

    return arr

print(spiralArray(3))