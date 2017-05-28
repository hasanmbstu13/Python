grades = [['A1' , 80], ['A2' , 70], ['A3' , 90]]
grades[0]
grades[1]
asn_to_grade = {'A1' : 80, 'A2' : 70, 'A3' : 90}
# Accessing dictionary element
asn_to_grade['A2']

'A4' in asn_to_grade

# Print keys of the dictionary
for assignment in asn_to_grade:
	print(assignment)

# Print value of the dictionary
for assignment in asn_to_grade:
	print(asn_to_grade[assignment])

# Print key and value of the dictionary
for assignment in asn_to_grade:
	print(assignment, asn_to_grade[assignment])

d = {'apple' : 2, 5 : 8}
d[(1,2)] = 'banana'
