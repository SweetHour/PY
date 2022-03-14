number=8
number_default=number
eterations = 512

for i in range(eterations):
    number*=number_default
print(f'{number_default} to the power of {eterations} equals: {number}')
