# using a appends, using w OVERWRITES the entire file
employee_file = open("tutorial/20-reading-writing/employees.txt", 'a')

#creating another file
# employee_file = open("tutorial/20-reading-writing/index.html", 'w')
# employee_file.write("<p>Hello</p>")

employee_file.write("\nKelly - Customer Service")
employee_file.close()
