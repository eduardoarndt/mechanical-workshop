from models.Person import Customer
class MenuCustomer:
    def __init__(self, repository):
        self.repository = repository

    def mainMenu(self):
        option = int(input("\nType the desired operation\n1.Register\n2.List\n"))

        if (option == 1):
            self.registerCustomer()
        elif option == 2:
            activeCustomerOption = int(
            input("Which customers to list?\n1.Actives\n2.Inactives\n"))
            self.repository.listCustomers(activeCustomerOption == 1)
            input("")

    def registerCustomer(self):
        print("Registering customer...")
        customerName = input('Enter customer''s name: ')
        customerCpf = input('Enter customer''s CPF: ')
        customerNumber = input('Enter customer''s number: ')
        customerMail = input('Enter customer''s e-mail: ')
        customerAddress = input('Enter customer''s address: ')
        customerBirthDate = input('Enter customer''s birthDate: ')
        customerGender = input('Enter customer''s gender: ')
        customerCivilState = input('Enter customer''s civilState: ')

        newCustomer = Customer(customerName, customerCpf, customerNumber, customerMail, customerAddress, customerBirthDate,
                            customerGender, customerCivilState, True)

        self.repository.customers.append(newCustomer)            