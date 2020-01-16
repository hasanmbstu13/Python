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