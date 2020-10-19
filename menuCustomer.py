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
                self.repository.deleteCustomer(customer.cpf)
                self.registerCustomer()
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
