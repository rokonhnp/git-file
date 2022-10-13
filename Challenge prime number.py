# number = int(input('Enter a number: '))
# dividing_number = int(input('Enter a number: '))
#
# modulas = number % dividing_number
# dividing_result = number / dividing_number
#
# print('modulas:', modulas)
# print('Deviding result:', dividing_result)
#---------------------------------
# number = int(input('Enter a number: '))
#
# count = 0
# i = 1
#
# while i <= number:
#     if number % i == 0: #if modulas = 0
#         count += 1
#     i += 1
#
# if count == 2:
#     print('It is prime number')
#
# else:
#     print('It\'s not prime number')


number = int(input('Enter Your Number : '))
prime_count = 0
checking = 1
while checking <= number:
    i = 1
    count = 0
    while i <= checking:
        if checking % i == 0:
            count += 1
        i += 1

    if count == 2:
        print(checking)
        prime_count += 1

    checking += 1

print('This number has', prime_count, 'prime number')