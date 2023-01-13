num1 = float(input('Type a number: '))
operator = input('What operation do you want: (+) (-) (*) (/)')
num2 = float(input('Type a number: '))

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else:
    print('Invalid operator')
