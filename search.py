#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return linear_search_iterative(array, item)
    # return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

def linear_search_recursive(array, item, index=0):
     if array[index] == item:
        return item
        if index == len(array):
            return None
        else:
            return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
#     """return the index of item in sorted array or None if item is not found"""
#     # implement binary_search_iterative and binary_search_recursive below, then
#     # change this to call your implementation to verify it passes all tests
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    # once implemented, change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    #picked the middle of the array, compared the target 
    # to the middle element if it was greater or smaller, and then discarded one half
    
    #[5,6,7,10,12] target 0
    left_index = 0
    right_index = len(array) - 1

    #loop, when can I stop the loop?
    while left_index <= right_index:

        mid_index = (left_index + right_index) // 2
        print("Middle index:", mid_index)
        print("Left index:", left_index)
        print("Right index:", right_index)
        #is the middle item what we are looking for?
        if array[mid_index] == item:
            print("Found it!")
            return mid_index
        #if item < item at middle, we ignore the right pat of the array
        elif item < array[mid_index]:
            print("Entered ignore right")
            right_index = mid_index -1
            print("Right index: ", right_index)
            print("Left index: ", left_index)
        elif item > array[mid_index]:
            print("Entered ignore left")
            left_index = mid_index + 1
    #if item > item at middle, we ignore the left part the array
    return None

def binary_search_recursive(array, item, left=None, right=None):
    left_index = 0
    right_index = len(array) - 1

    mid_index = (left_index + right_index) // 2
    print("Middle index:", mid_index)
    print("Left index:", left_index)
    print("Right index:", right_index)
    if array[mid_index] == item:
        print("Found it!")
        return mid_index
    #if item < item at middle, we ignore the right pat of the array
    elif item < array[mid_index]:
        print("Entered ignore right")
        right_index = mid_index -1
        print("Right index: ", right_index)
        print("Left index: ", left_index)
        binary_search_recursive(array, item, left_index, mid_index -1)
    elif item > array[mid_index]:
        print("Entered ignore left")
        left_index = mid_index + 1
    return None

linear_search([5,6,7,10,12],12);
binary_search([5,6,7,10,12],12)
