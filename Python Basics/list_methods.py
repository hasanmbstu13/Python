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
