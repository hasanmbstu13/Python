s = 'abccdeffggh'
for i in range(len(s) - 1):
    print(i)

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurences of a character
    and an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats


##The last valid index into s is s[len(s) - 1]. If we use
##for in range(len(s)), then on the last iteration i is slen(s)-1
##, and so , s[i+1] is the same thing is s[len(s) - 1 + 1] and this causes an error.
##def count_adjacent_repeats(s):
##    repeats = 0
##    for i in range(len(s)):
##        if s[i] == s[i + 1]:
##             repeats = repeats + 1
##   return repeats


##We must start at 1. If we started at 0 as before, then our first iteration would compare s[0] to s[-1]
##(the last character). And we must go up to but not including len(s) (because the final index is len(s) - 1. 
def count_adjacent_repeats(s):
    repeats = 0
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            repeats = repeats + 1

    return repeats

def shift_left(L):
    ''' (list) -> NoneType

    Shift each item in L one position to the left and shift
    the first item to the last position.

    Precondition: len(L) >= 1
    '''

    first_item = L[0]

    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item

def count_adjacent_repeats(s):
    ''' (str) -> int

    Return the number of occurrences of a character and
    an adjacent character being the same.

    >>> count_adjacent_repeats('abccdeffggh')
    3
    '''

    repeats = 0

    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            repeats = repeats + 1

    return repeats


def shift_left(L):
    first_item = L[0]
    for i in range(1, len(L)):
        L[i - 1] = L[i]

    L[-1] = first_item

letters = ['z', 'y', 'x', 'w']
shift_left(letters)


