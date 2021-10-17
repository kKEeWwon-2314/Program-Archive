"""
Implementation of some elementary sorting algorithms including bubble sort 
and selection sort. This program also demonstrates how we can sort an array 
of indices into the original data, rather than sorting the arrays of data 
values themselves, to preserve any index-based data association we might 
have between different arrays.
"""

def swap_elements(array, i, j):
    """
    Exchanges the elements at index i and j within the given array.
    """
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


def is_already_sorted(array):
    """
    Return True if the given array is already sorted, False otherwise.
    """
    # repeat for every adjacent pair of elements left to right
    for i in range(len(array)-1):
        # if they are out of order, array is not sorted
        if array[i] > array[i+1]:
            return False
    return True


def bubble_sort(array):
    """
    Runs the bubble sort algorithm to sort the elements of given array.
    """
    # repeat while the array is not sorted
    while not is_already_sorted(array):
        # for each pair of elements going from left to right
        for i in range(len(array)-1):
            # exchange the pair if they are not in order
            if array[i] > array[i+1]:
                swap_elements(array, i, i+1)


def index_of_lowest(array, start, end):
    """
    Find and return the index of the least element in the array between
    the indices [start, end].
    """
    lowest = array[start]
    lowest_index = start
    for i in range(start+1, end):
        if array[i] < lowest:
            lowest = array[i]
            lowest_index = i
    return lowest_index


def selection_sort(array):
    """
    Sorts the given array with the selection sort algorithm.
    """
    # repeat for each position from left to right
    for i in range(len(array)):
        # find the index of the least element from current position to end
        least_index = index_of_lowest(array, i, len(array))
        # swap the current position with the least index
        swap_elements(array, i, least_index)


def indices_already_sorted(indices, array):
    """
    Determines if the indices provided give a sorted ordering if the
    elements in the array.
    """
    # repeat for every adjacent pair of indices left to right
    for i in range(len(array)-1):
        # if the values in the array corresponding to these indices
        # are out of order, the index array is not sorted
        left_index = indices[i]
        right_index = indices[i+1]
        left_value = array[left_index]
        right_value = array[right_index]
        if left_value > right_value:
            return False

    # otherwise everything is already in order
    return True


def bubble_sort_indices(indices, array):
    """
    Sort the indices given by the values in the corresponding array.
    Note that array itself remains unaltered.
    On completion, we will have the ordered sequence:
        array[indices[0]] <= array[indices[1]] <= ... <= array[indices[N]]
    """
    # repeat while the array is not sorted
    while not indices_already_sorted(indices, array):
        # for each pair of indices going from left to right
        for i in range(len(array)-1):
            # look up the values in array corresponding to the index pair
            left_index = indices[i]
            right_index = indices[i+1]
            left_value = array[left_index]
            right_value = array[right_index]
            # and exchange the indices if the values are out of order
            if left_value > right_value:
                swap_elements(indices, i, i+1) 


# some test data from our Grade 8 homeroom
characters = ['Noah', 'Roman', 'Marko', 'Keeyan', 'Gage']
match = ['Barleen', 'Sofijia', 'Irmak', 'Sara', 'Kaytlin']

# print out the original, unordered name-match associations
for i in range(len(characters)):
    print(characters[i], match[i]


# create a set of indices and sort them ascending by name
indices_by_name = [0, 1, 2, 3, 4]
bubble_sort_indices(indices_by_name, characters)

print()
print('Indices sorted by name:', indices_by_name)
for index in indices_by_name:
    print(characters[index], match[index])

# create another set of indices and sort them ascending by match
indices_by_match = [0, 1, 2, 3, 4]
bubble_sort_indices(indices_by_match, match)

print()
print('Indices sorted by match:', indices_by_match)
for index in indices_by_match:
    print(characters[index], match[index])