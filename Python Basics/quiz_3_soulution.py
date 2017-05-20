def merge(L):
    merged = []
    for i in range(0, len(L), 3):
        merged.append(L[i] + L[i + 1] + L[i + 2])
    return merged

print(merge([1, 2, 3, 4, 5, 6, 7, 8, 9]))


def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    count = 0
    for i in range(len(s) // 2):
        count = count +1
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached?
            matches = matches + 1

    return count


def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]: # <--- How many times is         this line reached?
            matches = matches + 1

    return matches == (len(s) // 2)

mystery('civil')


def mystery(s):
    """ (str) -> bool
    """
    matches = 0
    for i in range(len(s) // 2):
        if s[i] == s[len(s) - 1 - i]:
            matches = matches + 1

    return matches == (len(s) // 2)


def shift_right(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the rightand shift the    last item to the first position.

    Precondition: len(L) >= 1
    '''

    last_item = L[-1]

    # MISSING CODE GOES HERE

    L[0] = last_item

count = 0
for i in range(2, 5):
    for j in range(4, 9):
        count = count + 1
        #print(i, j)
#print(count)


def contains1(value, lst):
    """ (object, list of list) -> bool
    Return whether value is an element of one of the nested        lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
    True
    """
    found = False
    # CODE MISSING HERE
    for i in range(len(lst)):
       for j in range(len(lst[i])):
           found = (lst[i][j] == value)
   
    return found

def contains2(value, lst):
    """ (object, list of list) -> bool
    Return whether value is an element of one of the nested        lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
    True
    """
    found = False
    # CODE MISSING HERE
    for item in lst:
        if value == item:
            value = True
   
    return found

def contains3(value, lst):
    """ (object, list of list) -> bool
    Return whether value is an element of one of the nested        lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
    True
    """
    found = False
    # CODE MISSING HERE
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            if lst[i][j] == value:
                found = True
   
    return found

def contains(value, lst):
    """ (object, list of list) -> bool
    Return whether value is an element of one of the nested        lists in lst.

    >>> contains('moogah', [[70, 'blue'], [1.24, 90, 'moogah'],    [80, 100]])
    True
    """
    found = False
    # CODE MISSING HERE
    for sublist in lst:
        if value in sublist:
            found = True
   
    return found

