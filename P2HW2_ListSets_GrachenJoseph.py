# CTI-110
# P2HW2 - Lists and Sets
# Joseph Grachen
# 10/04/2021
#

x1 = float(input('Enter number 1: '))
x2 = float(input('Enter number 2: '))
x3 = float(input('Enter number 3: '))
x4 = float(input('Enter number 4: '))
x5 = float(input('Enter number 5: '))
x6 = float(input('Enter number 6: '))

num_list = [x1, x2, x3, x4, x5, x6]

print('Created list')
print(num_list)
print('Smallest number in list: ', min(num_list))
print('Largest number in list: ', max(num_list))
print('Sum of numbers in list: ', sum(num_list))
print('Average of numbers in list: ', '{:.1f}'.format(sum(num_list) / len(num_list)))

num_set = set(num_list)

print('Created set')
print(num_set)
