'''i=0
numbers = [1, 2, 3, 4, 5]
total_Sum=0
for a in numbers:
    total_Sum += a
print(total_Sum)

for()'''
def min_max_sums(arr):
    arr.sort()
    min_sum = sum(arr[:4])
    max_sum = sum(arr[1:])
    print(min_sum, max_sum)

# Test the function
arr = [1, 2, 3, 4, 5]
min_max_sums(arr)


