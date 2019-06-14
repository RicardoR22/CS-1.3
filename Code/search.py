#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index == len(array):
        return None
    elif array[index] == item:
        return index
    return linear_search_recursive(array, item, index + 1)


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer <= right_pointer:
        mid_index = (left_pointer + right_pointer) // 2
        mid_value = array[mid_index]

        if mid_value == item:
            return mid_index
        elif mid_value < item:
            left_pointer = mid_index + 1
        else:
            right_pointer = mid_index - 1

    return None



def binary_search_recursive(array, item, left=None, right=None):

    if left is None:
        left = 0
        right = len(array) - 1

    if left > right:
        return None

    mid_index = (left + right) // 2
    mid_value = array[mid_index]

    if mid_value == item:
        return mid_index
    elif mid_value < item:
        left = mid_index + 1
        return binary_search_recursive(array, item, left, right)
    elif mid_value > item:
        right = mid_index - 1
        return binary_search_recursive(array, item, left, right)
