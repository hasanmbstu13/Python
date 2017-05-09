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
for i in range(524, 10509, 1):
    sum = sum + i


print(sum)
