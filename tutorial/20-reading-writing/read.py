# r is for read
# w for write
# a for append, you can only add info (cant change)
# r+ read and write

employee_file = open("tutorial/20-reading-writing/employees.txt", "r")

# print(employee_file.readable())
# print(employee_file.read())

# print(employee_file.readline())
# print(employee_file.readline())

# print(employee_file.readlines()) # gives an array we can use index in it

for employee in employee_file.readlines():
    print(employee)

employee_file.close()
