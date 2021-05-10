num1 = input('Enter num1: ')
operator = input('Choose operator want to use(+,-,*,/): ')
num2 = input('Enter num2: ')


if operator == '+':
    result = float(num1) + float(num2)
    print(result)
elif operator == '-':
    result = float(num1) - float(num2)
    print(result)
elif operator == '*':
    result = float(num1) * float(num2)
    print(result)
elif operator == '/':
    result = float(num1) / float(num2)
    print(result)