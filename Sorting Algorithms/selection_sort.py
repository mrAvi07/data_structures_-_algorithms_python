"""
    Selection Sort 
"""



def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index



def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))


    return new_arr
    


if __name__=="__main__":
    print(" Unsorted List ")
    number_list = [17, 3, 25, 4, 9, 10, 2]
    print(number_list)

    print("selection sort ")
    sorted_arr = selection_sort(number_list)
    print(sorted_arr)
