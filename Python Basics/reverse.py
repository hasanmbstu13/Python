def reverse(s):
     '''(str) -> str

     Return the reverse of s.

     >>> reverse('abc')
    'cba'
    >>> reverse('a')
    'a'
    >>> reverse('madam')
    'madam'
    >>> reverse('1234!')
    '!4321'
    '''
     result = ''
     i = len(s) - 1
     while i >= 0:
        result = result + s[i]
        i = i - 1 # CODE MISSING HERE

     return result
