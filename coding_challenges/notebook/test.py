def numberToWords(num):
    def numberToWords1K(num):
        word = dict()
        word[1] = "One"
        word[2] = "Two"
        word[3] = "Three"
        word[4] = "Four"
        word[5] = "Five"
        word[6] = "Six"
        word[7] = "Seven"
        word[8] = "Eight"
        word[9] = "Nine"
        word[10] = "Ten"
        word[11] = "Eleven"
        word[12] = "Twelve"
        word[13] = "Thirteen"
        word[14] = "Fourteen"
        word[15] = "Fifteen"
        word[16] = "Sixteen"
        word[17] = "Seventeen"
        word[18] = "Eighteen"
        word[19] = "Nineteen"
        word[20] = "Twenty"
        word[30] = "Thirty"
        word[40] = "Forty"
        word[50] = "Fifty"
        word[60] = "Sixty"
        word[70] = "Seventy"
        word[80] = "Eighty"
        word[90] = "Ninety"

        s_num = str(num)
        length = len(s_num)

        if((num>0) and (num<=20)):
            return word[num]
        
        out = []
        for i in range(length):
            n = (int(s_num[i])*(pow(10,length-i-1)))
            if((n>0) and (n<100)):
                if((i==(length-2)) and (s_num[i+1]!='0') and (s_num[i]=='1')):
                    n += (int(s_num[i+1])*(pow(10,length-i-2)))
                    out.append(word[n])
                    break
                out.append(word[n])
            elif((n>=100) and (n<1000)):
                out.append(word[n/100])
                out.append("Hundred")
        return " ".join(out).strip()

    if(num==0):
        return "Zero"

    res = []
    if((num//1000)==0):
        res.append(numberToWords1K(num))
    elif((num//1000000)==0):
        res.append(numberToWords1K(num//1000))
        res.append("Thousand")
        res.append(numberToWords1K(round((num/1000-(num//1000))*1000)))
    elif((num//1000000000)==0):
        res.append(numberToWords1K(num//1000000))
        res.append("Million")
        res.append(numberToWords1K(num//1000))
        res.append("Thousand")
        res.append(numberToWords1K(round((num/1000-(num//1000))*1000)))
    elif((num//1000000000000)==0):
        res.append(numberToWords1K(num//1000000000))
        res.append("Billion")
        res.append(numberToWords1K(num//1000000))
        res.append("Million")
        res.append(numberToWords1K(num//1000))
        res.append("Thousand")
        res.append(numberToWords1K(round((num/1000-(num//1000))*1000)))
    
    return " ".join(res).strip()

num = 1000000
print(numberToWords(num))