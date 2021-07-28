"""
    Binary Search Algorithm
    Time Complexity of Binary search algorithm is O( log n)

"""
def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list)-1
    mid_index = 0
    
    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index

        if mid_number < number_to_find:
            left_index = mid_index + 1

        else:
            right_index = mid_index - 1

    return -1
    



if __name__=="__main__":

    list_1 = [i for i in range(11, 21)]
    number = 26

    index = binary_search(list_1, number)
    if index == -1:
        print("Number not found!")
    else:
        print(f"Number found at {index} index")
    

