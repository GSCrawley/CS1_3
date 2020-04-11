#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # linear_search_iterative(array, item)
    # linear_search_recursive(array, item)
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)

def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found

def linear_search_recursive(array, item, index=0):
    
    if array[index] == item:
        # print("TEST1")
        print(array[index])
        return index
    if index == len(array)-1:
        # print("TEST2")
        return None
    else:
        # print("TEST3")
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    #"""return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    
    # return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)

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
        else:
            left_index = mid_index + 1
    #if item > item at middle, we ignore the left part the array
    

def binary_search_recursive(array, item, left=None, right=None):
    # TODO: implement binary search recursively here
    # If we are starting from the beggining
    if left is None and right is None:
        # left is 0
        left = 0
        # right is the length of the array
        right = len(array) -1
    '''START'''
    # finding the middle
    mid_index = (left + right) // 2
    # if the item is not in the list
    if left>right:
        # Its not in the list
        return None
    # if our middle index is the item
    if array[mid_index] == item:
        # print("TEST1")
        print("Found it!", mid_index)
        # You found it!
        return mid_index
    # elif the item index is larger then the middle
    elif item > array[mid_index]:
        # print('TEST2')
        # Go back to start but now left == the middle plus one.
        return binary_search_recursive(array, item, mid_index +1, right)

    else:#item index is smallen then middle
        # print('TEST3')
        #Go back to start but now right == the middle minus one. 
        return binary_search_recursive(array, item, left, mid_index - 1)

print(binary_search(['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick'], 'Brian'))
print(linear_search(['Winnie', 'Kojin', 'Brian', 'Nabil', 'Julia', 'Alex', 'Nick'], 'Brian'))

print(binary_search([1,2,3,4,5,6,7],7))
print(linear_search([1,2,3,4,5,6,7],7))
