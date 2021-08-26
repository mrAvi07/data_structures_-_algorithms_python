"""

    Quick Sort:
        Time Complexity :
            1) Average case : O(n log n)
            2) Worst Case : O(n^2)


"""





def quicksort(arr):
    size_arr = len(arr)

    if size_arr < 2:
        return arr

    if size_arr == 2:
        if arr[0] > arr[1]:
            arr[0], arr[1] = arr[1], arr[0]

        return arr


    pivot = arr[0]
    left_arr = [i for i in arr[1:] if i < pivot]
    right_arr = [i for i in arr[1:] if i > pivot]

    return quicksort(left_arr) + [pivot] + quicksort(right_arr)



if __name__=="__main__":

    arr = [9, 3,2 ,1, 8, 10, 4]
    sorted_arr = quicksort(arr)

    for i in range(len(sorted_arr)):
        print(sorted_arr[i] , end=" ")
