# locate the file
filanders_file = 'E:/My Docs/Applying Document For Higher Study/Applying Information.txt'
# open the file in read mode
# filanders_file = open(filanders_file, 'r')
# read the file
# filanders_file.readline()

# filanders_file.close()

filanders_file = open(filanders_file, 'r')
line = filanders_file.readline()
while line != '':
    # Function print also prints a newline.
    # print has an optional parameter that specifies the string
    # to print as the end marker.
    # to avoid extra new line we change the code print(line, end='')
    print(line, end='')
    line = filanders_file.readline()



# The for line in file approach
# for line in file:
#   process line
# When to use this approach
# When you want to process every line in a file.

filanders_file = 'E:/My Docs/Applying Document For Higher Study/Applying Information.txt'
filanders_file = open(filanders_file, 'r')
for line in filanders_file:
    print(line, end='')

# The read approach
# print(filanders_file.read())

# The readlines approach
# list = file.readlines()
# return all the lines of the file as a list
