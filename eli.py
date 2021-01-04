#Create the list that will become the employee list.
employees = []

#function to add employees to the list
def add_employee():
    print ("Welcome to the Employee Management System, Please fill in the following values")
    print ("Please enter the Employee name")
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
    employees.append(full_employee)
#function to list all employees
def list_employees():
    print(*employees, sep = "\n")
    print ("Thank you for using the employee management system!")
    print ("\n")
def find_employee():
    print ("please type the social security number of the employee you want to find")
    search = input()
    if search in employees:
        print ("yay")

while True:
    print ("Welcome to the employee Management system!")
    print ("------------------------------------------------------------------")
    print ("The current amount of employees in the list is: ", len(employees), "\n" )
    print ("------------------------------------------------------------------")
    print ("Type 1 to add an employee, type 2 to view all the employees")
    selection = input()
    if selection == "1": add_employee()
    if selection == "2": list_employees()
    if selection == "3": find_employee()
