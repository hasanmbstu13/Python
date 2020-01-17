file = open('file_example.txt', 'r') 
contents = file.read() 
print(contents)
file.close()

# with statement to read file, with automatically closes a file when the end of the block is reached.
with open('file_example.txt', 'r') as file:
	contents = file.read()

print(contents)

with open('../../lorem.txt', 'r') as file:
	contents = file.read()

print(contents)


# Test cursor pointing
with open('../../lorem.txt', 'r') as file:
	first_ten_chars = file.read(10)
	# cursor will start after 10 chars
	the_rest = file.read()


print("The first 10 characters:", first_ten_chars)
print("The rest of the file:", the_rest)


# Return contents of a file into a list of strings
with open('../../lorem.txt', 'r') as file:
	lines = file.readlines()

print(lines)
print(lines[0])