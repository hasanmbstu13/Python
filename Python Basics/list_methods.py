colours = []
prompt = 'Enter another of your favourite colours (type return to end): '
colour = input(prompt)

while colour != '':
    colours.append(colour)
    colour = input(prompt)

colours.extend(['hot pink', 'neon green'])

colours.pop()
colours.pop(2) # Here 2 is the index number and will remove the second value from the list

colours.remove('black')

if colours.count('yellow'):
    colours.remove('yellow')

# This is more standard then previous one
if 'yellow' in colours:
    colours.remove('yellow')

colours.extend(['auburen', 'taupe', 'magenta'])
colours.sort()
colours.reverse()
colours.insert(-2, 'brown')

if 'hot pink' in colours:
    where = colours.index('hot pink')
    colours.pop(where)


list1 = [1, 2, 3]
list2 = list1
list2.append(4)

# Answer will 4
# list1 and list2 refer to the same list object, so changes to that list will be seen by both variables.

def double_even_indices(lst):
    """ (list of int) -> NoneType

    Double every other int in lst, starting at index 0.
    """

    i = 0
    while i < len(lst):
        lst[i] = lst[i] * 2
        i = i + 2

    list1 = [11, 12, 13, 14, 15, 16, 17]
    print(list1)
    double_even_indices(list1)
    print(list1)


def double_first_element(lst):
    if len(lst) > 0:
       lst[0] = lst[0] * 2

list1 = [10, 100, 1000]
double_first_element(list1)

# Answer will 20
# lst and list1 refer to the same list object, so the statement
# lst[0] = lst[0]*2 will change the list that list1 refers to.

def interrupted(s):
    s[-1] = "-"

greeting = "how are you"
interrupted(greeting)
print(greeting)

# Python raises an error
# Any attempt to modify an immutable type will raise a TypeError

lst1 = [11, 12, 13, 14, 15, 16, 17]
lst2 = lst1
lst1[-1] = 18
lst2

# After the second statement executes, lst1 and lst2
# both refer to the same list. When two variables
# refer to the same objects, they are aliases. If that list is modified,
# both of lst1 and lst2 will see the change.
