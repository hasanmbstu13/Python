# starting index or value is 0 and ending limit is
# up to 10 here it is 9.

sum = 0
for num in range(11):
    sum = sum + num
    
print(sum)

s = 'computer science'
len(s)

#for i in range(len(s)):
#    print(i)
    

# range([start,] stop[, stop]) -> range object return a virtual sequence
# of numbers from start to stop by step.

# will return odd indexes and increment by 2
#for i in range(1, len(s), 2):
#    print(i)

sum = 0
for i in range(1526, 10505, 3):
    sum = sum + i


print(sum)


values = []
for num in range(1, 4):
    values.append(num * 3)
print(values)


values = []
for num in range(3, 10, 3):
    values.append(num)
print(values)


values = []
for num in range(3, 9, 3):
    values.append(num)
print(values)

values = []
for num in range(1, 3):
    values.append(num * 3)
print(values)

sum = 1523
i = 1523
while i <= 10503:
    if (i % 3 == 0):
        sum = sum + i
    
    i = i +1
print(sum)
