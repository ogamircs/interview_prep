import time
import random

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

#create sublists and gapped items and then uses insertion sort to sort the items in the sublist
#the sublist size keeps changing until everything is sorted O(n^3/2)
def shell_sort(input_array):
    a_list = input_array.copy()
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        #print("After increments of size", sublist_count, "The list is", a_list)
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

def merge_sort(input_array):
    a_list = input_array.copy()
    merge_sort_helper(a_list)
    return a_list


def merge_sort_helper(alist):
    size = len(alist)
    mid_point = size // 2
    if(size>1):
        # Dividing the array elements
        L = alist[0:mid_point]
        # into 2 halves
        R = alist[mid_point:size]

        merge_sort_helper(L)
        merge_sort_helper(R)

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                alist[k] = L[i]
                i += 1
            else:
                alist[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            alist[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            alist[k] = R[j]
            j += 1
            k += 1

def quick_sort(input_array):
    a_list = input_array.copy()
    quick_sort_helper(a_list, 0, len(a_list) - 1)
    return a_list

def quick_sort_helper(a_list, first, last):
    if first < last:
        split_point = partition(a_list, first, last)
        quick_sort_helper(a_list, first, split_point - 1)
        quick_sort_helper(a_list, split_point + 1, last)


def partition(a_list, first, last):
    pivot_value = a_list[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and a_list[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while a_list[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = a_list[left_mark]
            a_list[left_mark] = a_list[right_mark]
            a_list[right_mark] = temp

    temp = a_list[first]
    a_list[first] = a_list[right_mark]
    a_list[right_mark] = temp

    return right_mark

if __name__ == '__main__':
    print("original list:")
    #mylist = [19, 1, 9, 7, 3, 10, 13, 8, 15, 8, 12]
    #mylist = [4,2,1,3]
    mylist = []
    for i in range(0, 10000):
        n = random.randint(1, 30)
        mylist.append(n)

    print(mylist)
    print("bubble sort:")
    start_time = time.time()
    bubble_sort(mylist)
    #print(bubble_sort(mylist))
    end_time = time.time()
    print(end_time-start_time)

    print("selection sort:")
    start_time = time.time()
    selection_sort(mylist)
    #print(selection_sort(mylist))
    end_time = time.time()
    print(end_time - start_time)

    print("insertion sort:")
    start_time = time.time()
    insertion_sort(mylist)
    #print(insertion_sort(mylist))
    end_time = time.time()
    print(end_time - start_time)

    print("shell sort:")
    start_time = time.time()
    shell_sort(mylist)
    #print(shell_sort(mylist))
    end_time = time.time()
    print(end_time - start_time)

    print("merge sort:")
    start_time = time.time()
    merge_sort(mylist)
    #print(merge_sort(mylist))
    end_time = time.time()
    print(end_time - start_time)

    print("quick sort:")
    start_time = time.time()
    quick_sort(mylist)
    #print(quick_sort(mylist))
    end_time = time.time()
    print(end_time - start_time)

