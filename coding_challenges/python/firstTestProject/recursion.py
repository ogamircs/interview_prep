from HashTable import HashTable


def list_sum(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])

def to_str(n, base):
    convert_string = "0123456789ABCDEF"

    if n < base:
        return convert_string[n]
    else:
        return to_str(n//base, base) + convert_string[n%base]

def reverse(input_string):
    size = len(input_string)
    if size==1:
        return input_string
    else:
        return input_string[size-1] + reverse(input_string[0:size-1])

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

def move_disk(fp,tp):
    print(f"moving disk from {fp} to {tp}.")

def binary_search(ordered_list, item):
    size = len(ordered_list)
    if size==0:
        return False
    elif (item < ordered_list[size//2]):
        return binary_search(ordered_list[0:size//2], item)
    elif (item > ordered_list[size // 2]):
        return binary_search(ordered_list[size//2+1:size], item)
    elif (item == ordered_list[size // 2]):
        return True

def hash(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum = sum + ord(a_string[pos])*(pos+1)
    return sum % table_size

if __name__ == '__main__':
    print("sum of a list:")
    l = [1,2,3]
    print(list_sum(l))
    print("change base:")
    print(to_str(345, 2))
    print(to_str(3453, 16))
    print("reverse:")
    print(reverse("test"))
    print("Hanoi Tower:")
    move_tower(3, "A", "B", "C")
    print("binray search:")
    print(binary_search([1,2,3,4],4))
    print("Hashing:")
    print(hash("afadasdsaa",4))
    h = HashTable()
    h[54] = "cat"
    h[26] = "dog"
    h[93] = "lion"
    h[17] = "tiger"
    h[77] = "bird"
    h[31] = "cow"
    h[44] = "goat"
    h[55] = "pig"
    h[20] = "chicken"
    print(h.slots)
