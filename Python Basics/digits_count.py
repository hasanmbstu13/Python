def digits_count(number):
    ''' (int) -> int

    Return total number of digits from a given number.

    >>> digits_count(17)
    2
    >>> digits_count(4027)
    4
    >>> digits_count(402789)
    6
    '''
    count = 0
    
    while number >= 10:
        number = number / 10
        count = count +1


    if (number < 10):
        count = count +1


    print(count)
