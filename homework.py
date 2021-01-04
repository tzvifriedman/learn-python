## This is a python script
employees = []


# This is a class. A class is an object that contains attributes and methods
# (things that it is and things that it does). Right now, we just care that
# that we can create an object of type "employee" and objects of type employee
# have the attributes we're looking to input.
#
# The following lines of code just define a thing called an employee that can
# be created by passing "name, ssn, phone, etc." as parameters (see line 33).

class employee:
    def __init__(self, name, ssn, phone, email, salary):
        self.name = name
        self.ssn = ssn
        self.phone = phone
        self.email = email
        self.salary = salary

def add_employee():
    print ("Welcome to the Empoyee Management System, Please fill in the following values")
    print ("Pleast enter the Employee name")
    employeeName = input()
    print ("Now, enter the employees Social Security Number")
    employeeSSN = input()
    print ("What is the employee's phone number?")
    employeePhone = input()
    print ("What about the Employee's email address?")
    employeeEmail = input()
    print ("Lastly, what is the Employee's Salary?")
    employeeSalary = input()
    full_employee = f''' ------------------{employeeName}--------------\n {employeeSSN} \n {employeePhone} \n {employeeEmail} \n {employeeSalary} \n --------------------------------------'''
    # we're adding to our employees list an object "employee" and adding all of
    # our info to that object's attributes. If we want, we can refer to
    # a single attribute of a single item of the list with "employees[1].name"
    # and that should return the name of the second employee in the list
    employees.append(employee(employeeName, employeeSSN, employeePhone,
        employeeEmail, employeeSalary)
    )

def list_employees():
    for x in employees:
       # __dict__ is a built-in object method that prints all the attributes
       # and their values. If you just try to print(x) you won't get useful
       # data. Just "Hey this is an object". You could definitely pretty this up more if you
       # wanted to.
        print(x.__dict__)
        print ("Thank you for using the employee management system!")
        print ("\n")

def find_employee(ssn):
    # We are going to search for an SSN by looping through each employee object
    # and comparing the input SSN to the item's SSN
    match = False
    for x in employees:
        if ssn in x.ssn:
            match = True
            print("Here is the employee info: \n")
            print(f''' ------------------{x.name}--------------\n {x.ssn} \n
                    {x.phone} \n {x.email} \    n {x.salary} \n --------------------------------------''')
    if match == False:
        print("There is no employee match for that SSN")

def edit_employee(ssn):
    match = False
    for x in employees:
        if ssn in x.ssn:
            match = True
            print ("Please enter the new Employee name")
            employeeName = input()
            print ("Now, enter the employees new Social Security Number")
            employeeSSN = input()
            print ("What is the employee's new phone number?")
            employeePhone = input()
            print ("What about the Employee's new email address?")
            employeeEmail = input()
            print ("Lastly, what is the Employee's new Salary?")
            employeeSalary = input()
                        # full_employee = f''' ------------------{employeeName}--------------\n {employeeSSN} \n {employeePhone} \n {employeeEmail} \    n {employeeSalary} \n --------------------------------------'''

            x.name = employeeName
            x.ssn = employeeSSN
            x.phone = employeePhone
            x.email = employeeEmail
            x.salary = employeeSalary

    if match == False:
        print("No employee matched your search")


while True:
    print ("Welcome to the employee Management system!")
    print ("------------------------------------------------------------------")
    print ("The current amount of employees in the list is: ", len(employees), "\n" )
    print ("------------------------------------------------------------------")
    print ("Type 1 to add an employee, type 2 to view all the employees")
    selection = input()
    if selection == "1": add_employee()
    if selection == "2": list_employees()
    if selection == "3":
        print("Please enter a SSN:")
        searchSSN = input()
        find_employee(searchSSN)
    if selection == "4":
        print("Please enter a SSN to edit:")
        searchSSN = input()
        edit_employee(searchSSN)
