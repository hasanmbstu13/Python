s = 'C3H7'
digit_index = -1 # This will be -1 until we find a digit. >>> for i in range(len(s)):
for i in range(len(s)):
	if digit_index == -1 and s[i].isdigit(): 
		digit_index = i

print(digit_index)
