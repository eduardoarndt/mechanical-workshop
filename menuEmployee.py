from models.Person import Employee




class MenuEmployee:
    def __init__(self, repository):
        self.repository = repository

    def mainMenu(self):
        try:
            option = int(input("\nType the desired operation"
                            "\n1.Register employee"
                            "\n2.Update"
                            "\n3.Delete"
                            "\n4.List\n"))

            if option == 1:
                self.registerEmployee()
            elif option == 2:
                self.updateEmployee()
            elif option == 3:
                self.deleteEmployee()
            elif option == 4:
                self.repository.listEmployees()
                input("")
            else:
                print("Please enter a valid option! Returning to main menu!")
        except:
            print("Please enter a valid option! Returning to main menu! **Exception")

    def registerEmployee(self):
        print("Registering employee...")
        employeeName = input('Enter employee''s name: ')
        employeeCpf = input('Enter employee''s CPF: ')
        employeeNumber = input('Enter employee''s number: ')
        employeeEmail = input('Enter employee''s email: ')

        self.repository.idCounter += 1
        newEmployee = Employee(employeeName, employeeCpf,
                               employeeNumber, employeeEmail, self.repository.idCounter)
        self.repository.employees.append(newEmployee)

    def updateEmployee(self):
        print("Updating employee...")
        employeeCpf = input('Enter employee''s CPF: ')

        employeeToUpdate = self.repository.findEmployee(employeeCpf)

        if employeeToUpdate is not None:
            employeeName = input('Enter employee''s updated name: ')
            employeeCpf = input('Enter employee''s updated CPF: ')
            employeeNumber = input('Enter employee''s updated number: ')
            employeeEmail = input('Enter employee''s updated email: ')

            employeeToUpdate.name = employeeName
            employeeToUpdate.cpf = employeeCpf
            employeeToUpdate.number = employeeNumber
            employeeToUpdate.mail = employeeEmail
        else:
            print("Employee with the specified CPF not found!")


    def deleteEmployee(self):
        print("Deleting employee...")
        employeeCpf = input('Enter employee''s CPF: ')

        employeeToBeDemitido = self.repository.findEmployee(employeeCpf)

        if employeeToBeDemitido is not None:
            areYouSure = int(input("ARE YOU SURE YOU WANT TO DELETE EMPLOYEE "
                                   + employeeToBeDemitido.name + "?\n1. Yes\n2. No\n")) == 1

            if areYouSure:
                self.repository.deleteEmployee(employeeToBeDemitido.cpf)
            else:
                print("Ok, cancelling operation!")
        else:
            print("Employee with the specified CPF not found!")
