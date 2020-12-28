from Fraction import Fraction
from Stack import Stack

def anagram_solution4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] + 1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False
    return still_ok

def par_checker(symbol_string):
    s = Stack()

    st = list(symbol_string)
    for i in range(0,len(st)):
        if(st[i] in '([{'):
            s.push(st[i])
        elif(st[i] in ')]}' and s.is_empty()==False):
            top = s.pop()
            if( (top=='(' and st[i]!=')') or (top=='[' and st[i]!=']') or (top=='{' and st[i]!='}')):
                return False
        elif(st[i] in ')]}' and s.is_empty()):
            return False
        else:
            raise Exception("ERROR in STRING:" + symbol_string)

    if(s.is_empty()):
        return True
    else:
        return False

def divide_by_2(dec_number, base):
    rem_stack = Stack()
    digits = "0123456789ABCDEF"

    while(dec_number>0):
        rem_stack.push(dec_number % base)
        dec_number = dec_number // base
    bin_number = ""
    while(not rem_stack.is_empty()):
        bin_number = bin_number + str(digits[rem_stack.pop()])

    return bin_number


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("anagram_solution:")
    print(anagram_solution4("apple","ppale"))
    print("Fraction:")
    my_fraction = Fraction(3, 5)
    print(my_fraction)
    print("Stack:")
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    print(s.peek())
    print("par_checker:")
    print(par_checker("(()[])"))
    print("binary_number:")
    print(divide_by_2(233, 2))
    print(divide_by_2(233, 16))


