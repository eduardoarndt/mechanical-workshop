from models.Person import Employee
class MenuEmployee:
    
    def __init__(self, repository):
        self.repository = repository

    def mainMenu(self):
        option = int(input("\nType the desired operation\n1.Register\n2.List\n"))

        if option == 1:
            self.registerEmployee()
        elif option == 2:
            self.repository.listEmployees()
            input("")

    def registerEmployee(self):
        print("Registering employee...")
        employeeName = input('Enter employee''s name: ')
        employeeCpf = input('Enter employee''s CPF: ')
        employeeNumber = input('Enter employee''s number: ')
        employeeEmail = input('Enter employee''s email: ')

        self.repository.idCounter += 1
        newEmployee = Employee(employeeName, employeeCpf,
                            employeeNumber, employeeEmail, repository.idCounter)
        self.repository.employees.append(newEmployee)        