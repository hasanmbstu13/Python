s = 'hello'
##for char in s:
##    print(char)

i = 0

while not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i = i + 1

s = 'there'
i = 0
while not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i = i + 1

s = 'xyz'
i = 0
while i < len(s) and not (s[i] in 'aeiouAEIOU'):
    print(s[i])
    i = i + 1

def up_to_vowel(s):
    ''' (str) -> str

    Return a substring of s from index 0 up to but
    not including the first vowel in s.

    >>> up_to_vowel('hello')
    'h'
    >>> up_to_vowel('there')
    'th'
    >>> up_to_vowel('cs')
    'cs'
    '''

    before_vowel = ''
    i = 0

    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        before_vowel = before_vowel + s[i]
        i = i + 1

    return before_vowel

def get_answer(prompt):
    ''' (str) -> str

    Use prompt to ask the user for a "yes" or "no"
    answer and continue asking until the user gives
    a valid response. Return the answer.
    '''

    answer = input(prompt)

    while not (answer == 'yes' or answer == 'no'):
        answer = input(prompt)

    return answer

sum = 0
i = 1523
while i <= 10503:
	if (i % 3 == 0):
		sum = sum + i		
	i = i + 1

print(sum)



