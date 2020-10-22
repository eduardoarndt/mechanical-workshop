from models.Person import Customer
import logging


class MenuCustomer:
    def __init__(self, repository):
        self.repository = repository

    def mainMenu(self):
        option = int(input("\nType the desired operation"
                           "\n1.Register"
                           "\n2.Update"
                           "\n3.Delete"
                           "\n4.List\n"))

        if option == 1:
            self.registerCustomer()
        elif option == 2:
            self.updateCustomer()
        elif option == 3:
            self.deleteCustomer()
        elif option == 4:
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

        newCustomer = Customer(customerName, customerCpf, customerNumber, customerMail, customerAddress,
                               customerBirthDate, customerGender, customerCivilState, True)

        self.repository.registerCustomer(newCustomer)

    def updateCustomer(self):
        print("Updating customer...")
        customerCpf = input('Enter customer''s CPF: ')

        customer = self.repository.findCustomer(customerCpf)

        if customer:
            print("Please, update the customer information")
            try:
                self.readDataAndUpdateCustomer(customer)
            except:
                print("Error occurred while updating customer...")
                logging.debug("We may want to review this code to not lose customer data in the future but for now "
                          "it's what we got")

    def deleteCustomer(self):
        customerCpf = input('Enter customer''s CPF: ')

        areYouSure = int(input("ARE YOU SURE YOU WANT TO DELETE CUSTOMER " + customerCpf + "?\n1. Yes\n2. No\n")) == 1

        if areYouSure:
            self.repository.deleteCustomer(customerCpf)
        else:
            print("Ok, cancelling operation!")

    # this should be in the repository?
    def readDataAndUpdateCustomer(self, customer):
        print("Updating customer of name: " + customer.name + ", CPF: " + customer.cpf)
        customer.name = input('Enter customer''s name: ')
        customer.cpf = input('Enter customer''s CPF: ')
        customer.number = input('Enter customer''s number: ')
        customer.mail = input('Enter customer''s e-mail: ')
        customer.address = input('Enter customer''s address: ')
        customer.birthDate = input('Enter customer''s birthDate: ')
        customer.gender = input('Enter customer''s gender: ')
        customer.civilState = input('Enter customer''s civilState: ')

        try:
            isActive = int(input('Enter if customer is active: 1 for active, 2 for inactive: ')) == 1
            customer.isCustomerActive = isActive
        except:
                print("Invalid parameter... will leave customer as is")

        print("Customer information updated!")