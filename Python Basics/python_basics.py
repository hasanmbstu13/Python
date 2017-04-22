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

             
