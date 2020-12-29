from Deque import Deque
from Fraction import Fraction
from Queue import Queue
from Stack import Stack
from UnorderedList import UnorderedList


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

def infix_to_postfix(infix_expr):
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    op_stack = Stack()
    postfix_list = []
    token_list = infix_expr.split()

    for token in token_list:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfix_list.append(token)
        elif token == '(':
            op_stack.push(token)
        elif token == ')':
            top_token = op_stack.pop()
            while top_token != '(':
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        else:
            while (not op_stack.is_empty()) and \
                    (prec[op_stack.peek()] >= prec[token]):
                postfix_list.append(op_stack.pop())
            op_stack.push(token)

    while not op_stack.is_empty():
        postfix_list.append(op_stack.pop())
    return " ".join(postfix_list)

def hot_potato(name_list, num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for i in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()
    return sim_queue.dequeue()

def pal_checker(a_string):
    char_deque = Deque()
    for ch in a_string:
        char_deque.add_rear(ch)

    still_equal = True
    while char_deque.size() > 1 and still_equal:
        first = char_deque.remove_front()
        last = char_deque.remove_rear()
        if first != last:
            still_equal = False
    return still_equal

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
    print("infix_to_postfix:")
    print(infix_to_postfix("A * B + C * D"))
    print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
    print("Queue:")
    q = Queue()
    q.enqueue('hello')
    q.enqueue('dog')
    q.enqueue(3)
    print(q.dequeue())
    print("Hot Potatoe:")
    print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent", "Brad"], 3))
    print("Deque:")
    d = Deque()
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front(True)
    print(d.remove_rear())
    print(d.remove_front())
    print("pal_checker")
    print(pal_checker("radar"))
    print(pal_checker("data"))
    print("UnorderedList:")
    mylist = UnorderedList()
    mylist.add(2)
    mylist.add(17)
    s = mylist.size()
    print(f"list size {s}")
    print(mylist.search(17))





