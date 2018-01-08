def inhospitable_weather(temp):
    ''' (number) -> bool

    Return True if and only if the given temperature in degrees Celsius is
        unpleasent (too hot or too cold).

    >>> inhospitable_weather(20)
    False
    '''

    return temp > 28 or temp < 12
