print('select the operations to be performed')
print('1 is ADDITION')
print('2 is SUBTRACTION')
print('3 is MULTIPLICATION')
print('4 is DIVISION')

operation = input()

if operation == '1':
    number_1 = int(input('Enter the first number '))
    number_2 = int(input('Enter the second number '))
    z = number_1 + number_2
    print(z)

elif operation == '2':
    number_1 = int(input('Enter the first number '))
    number_2 = int(input('Enter the second number '))
    z = number_1 - number_2
    print(z)

elif operation == '3':
    number_1 = int(input('Enter the first number '))
    number_2 = int(input('Enter the second number '))
    z = number_1 * number_2
    print(z)

elif operation == '4':
    number_1 = int(input('Enter the first number '))
    number_2 = int(input('Enter the second number '))
    z = number_1 / number_2
    print(z)

else: 
    print('invalid entry')
