try:
    # value = 10/0
    number = int(input('Type a number: '))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError as err:
    print(err)
