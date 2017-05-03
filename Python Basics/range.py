# starting index or value is 0 and ending limit is
# up to 10 here it is 9.

for num in range(10):
    print(num)

s = 'computer science'
len(s)

for i in range(len(s)):
    print(i)
    

# range([start,] stop[, stop]) -> range object return a virtual sequence
# of numbers from start to stop by step.

# will return odd indexes and increment by 2
for i in range(1, len(s), 2):
    print(i)
