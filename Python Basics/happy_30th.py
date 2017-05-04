message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    new_message = new_message + char

print(new_message)

##message = 'Happy 29th!'
##new_message = ''
##
##for char in message:
##    new_message = new_message + str((int(char) + 1) % 10)
##
##print(new_message)

message = 'Happy 29th!'
new_message = ''

for char in message:
    if not char.isdigit():
        new_message = new_message + char
    else:
        new_message = new_message + str((int(char) + 1) % 10)

print(new_message)


message = 'Happy 29th!'
new_message = ''

for char in message:
    if char.isdigit():
        new_message = new_message + str((int(char) + 1) % 10)
    else:
        new_message = new_message + char

print(new_message)
