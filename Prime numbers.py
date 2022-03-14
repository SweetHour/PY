import numpy as np
numbers = [1235,3462,346323,4346,5346,4234,723,823,9,101,17]
array = np.array(numbers)

print(numbers)

for number in array:
    for i in range(round(number/2)):
        if number % (i+1) == 0 and i+1 !=1 and i+1!=number:
            numbers[numbers.index(number)] = 0
            break

print(numbers)