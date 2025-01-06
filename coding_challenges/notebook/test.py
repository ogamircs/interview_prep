def rotationalCipher(s, rotationFactor):
    newS = ""
    small_chars = "abcdefghijklmnopqrstuvwxyz"
    big_chars = small_chars.upper()
    n = len(small_chars)
    for c in s:
        if(c in small_chars):
            newIndex = small_chars.index(c)+rotationFactor
            while(newIndex>(n-1)):
                newIndex = newIndex-n
            newS += small_chars[newIndex]
        elif(c in big_chars):
            newIndex = big_chars.index(c)+rotationFactor
            while(newIndex>(n-1)):
                newIndex = newIndex-n
            newS+= big_chars[newIndex]
        else:
            newS += c
    return newS

input = "abcdefghijklmNOPQRSTUVWXYZ0123456789" 
rotationFactor = 39
print(rotationalCipher(input, rotationFactor))