def larger_of_smallest(L1, L2):
    '''(list of int, list of int) -> int

    Return the larger of the smallest value in L1 and the small    est value inL2.

    Precondition: L1 and L2 are not empty.

    >>> larger_of_smallest([1, 4, 0], [3, 2])
    2
    >>> larger_of_smallest([4], [9, 6, 3])
    4
    '''
    return max(min(L1),min(L2))
