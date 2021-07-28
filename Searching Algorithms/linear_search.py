"""
    Linear Search Algorithm
    Time Complexity of linear search algorithm is O(n)

"""



def linear_search(number_list, number_to_find):
    for index , element in enumerate(number_list):
        if element == number_to_find:
            return index
    return -1


if __name__=="__main__":
    list_1 = [1, 4, 2, 6, 10, 5, 13]
    number = 40

    index = linear_search(list_1, number)
    if index != -1:
        print(f"Number is Found at {index} index")

    else:
        print("Number Not Found")
