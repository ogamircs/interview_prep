def bubble_sort(input_array):
    size = len(input_array)
    arr = input_array.copy()

    for i in range(0, size):
        for j in range(0, i):
            if(arr[i]<arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    return arr

def selection_sort(input_array):
    a_list = input_array.copy()
    for fill_slot in range(len(a_list) - 1, 0, -1):
        pos_of_max = 0
        for location in range(1, fill_slot + 1):
            if a_list[location] > a_list[pos_of_max]:
                pos_of_max = location
        a_list[fill_slot], a_list[pos_of_max] = a_list[pos_of_max], a_list[fill_slot]
    return a_list

def insertion_sort(input_array):
    a_list = input_array.copy()
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    return a_list

def shell_sort(input_array):
    a_list = input_array.copy()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        print("After increments of size", sublist_count, "The list is", a_list)
        sublist_count = sublist_count // 2
    return a_list

#similar to insertion sort
def gap_insertion_sort(a_list, start, gap):
    for i in range(start + gap, len(a_list), gap):
        current_value = a_list[i]
        position = i
        while position >= gap and a_list[position - gap] > current_value:
            a_list[position] = a_list[position - gap]
            position = position - gap
            a_list[position] = current_value

if __name__ == '__main__':
    print("original list:")
    #mylist = [19, 1, 9, 7, 3, 10, 13, 8, 15, 8, 12]
    mylist = [4,2,1,3]
    print(mylist)
    print("bubble sort:")
    print(bubble_sort(mylist))
    print("selection sort:")
    print(selection_sort(mylist))
    print("insertion sort:")
    print(insertion_sort(mylist))
    print("shell sort:")
    print(shell_sort(mylist))

