print("hello") # print a sequence of arguments for user to read.

print("hello", "there")



def square_return(num):
    return num ** 2;

def square_print(num):
    print("The square of num is", num**2)

# During execution of a function call,
# if the end of the function body is reached without executing a return statement,
# that function call produces value none.

def add(num1, num2):
	print(num1+num2)

result = add(1,3)
# new_result = result + 1; #that will produce typeError because of adding with none

def add(number1, number2):
    return number1 + number2
    print("hello")

result = add(1, 3);

#name = input("What is your name? ");
#location = input("What is your location? ")
#print(name, "lives in", location)

#age = input("How old are you? ") # Regardless of the text entered by the user, the input function returns str

print('''how
are
you?''')


def area(base,height):
    '''(number, number) -> number

    Return the area of a triangle with dimensions base and height.
    '''
    return base * height / 2

# for doc string
'''(number, number) -> number

    Return the area of a triangle with dimensions base and height.
'''

def convert_to_celsius(fahrenheit):
    '''(number) -> float

    Return the number of Celsius degree equivalent to fahrenheit

    >>> convert_to_cersius(32)
    0.0
    >>> convert_to_celsius(212)
    100.0
    '''

    return (fahrenheit - 32) * 5 / 9

def perimeter(side1, side2, side3):
    '''(number, number, number) -> number

    Return the perimeter of the traingle with sides of length side1, side2, side3.

    >>> perimeter(3,4,5)
    12
    >>> perimeter(10.5, 6, 9.3)
    25.8
    '''

    return side1 + side2 + side3

def semiperimeter(side1, side2, side3):
    ''' (number, number, number) -> float

    Return the semiperimeter of a triangle with sides of length side1, side2, side3

    >>> semiperimeter(3,4,5)
    6.0
    >>> semiperimeter(10.5, 6, 9.3)
    12.9
    '''

    return perimeter(side1, side2, side3)/2


def count_letters(word):
    """ (str) -> int

    Return the number of letters in word.
    
    >>> count_letters('hello')
    5
    >>> count_letters('bonjour')
    7
    """

    return count_vowels(word)+count_consonants(word)

def converts_to_minutes(num_hours):
    """ (int) -> int
    Return the number of minutes there are in num_hours hours.
    >>>convert_to_minutes(2)
    120
    """

    minutes = num_hours * 2;
    return minutes

def converts_to_seconds(num_hours):
    """ (int) -> int
    Return the number of seconds there are in num_hours hours.
    >>>convert_to_minutes(2)
    7200
    """

    minutes = convert_to_minutes(num_hours);
    seconds = minutes * 60;
    return seconds

seconds = convet_to_seconds(2)


 grade = 80
 passed = grade >= 50

 # Passed will return True

# Type Converstion
# input("Enter the number of shoes: ") # returns input will return string
# solution is
num_shoes_left = 627
# num_shoes_wanted = int(input("Enter the number of shoes: "))
# num_shoes_left >= num_shoes_wanted # return flase

# In Operator

'cad' in 'abracadre'

'zoo' in 'ooze'

''  in 'adr'

s = "Learn to Program"
s[9:16]
s[9:len(s)]
s[9:]
s[:8]
s[:]
s[1:8]
s[1:-8]
s[-15:-8]
s = s[:5] + 'ed' + s[5:]

white_rabbit = "I'm late! I'm late! For a very important date!"
white_rabbit.count("ate")
"computer".capitalize()
white_rabbit.find('late')
white_rabbit.find('Late') # will return -1 due to its not find in the string
white_rabbit.rfind('late') # will return last late here it is 14
white_rabbit.find('late', 7)
s = "      I'm sleeping in late  " 
s.lstrip()                 # remove space of the beginning from the first
s.rstrip() # remove space of the last from the right
s.strip() # remove space from both end

# for loop over a string:
s = 'Hi there!'
for char in s:
	print(char)



             
