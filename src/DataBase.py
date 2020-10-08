from models.Person import *
from Printer import *

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
       if cls not in instances:
            instances[cls] = cls(*args, **kw)
       return instances[cls]
    return _singleton

##@singleton
class DataBase(object):

    customers = []
    employees = []

    def listCustomers(self):
        printer = Printer()

        printer.addPrintingObject("Name", True, 25)
        printer.addPrintingObject("CPF",  True, 11)
        printer.addPrintingObject("Number", False, 9)
        printer.addPrintingObject("Mail", True, 25)
        printer.addPrintingObject("Address", True, 30)
        printer.addPrintingObject("Birth date", True, 10)
        printer.addPrintingObject("Gender", False, 10)
        printer.addPrintingObject("Civil State", False, 15)

        for customer in self.customers: 
            if (customer.isCustomerActive == True):
                print(customer)

    def listEmployees(self):
        printer = Printer()

        printer.addPrintingObject("Name", True, 25)
        printer.addPrintingObject("CPF",  True, 11)
        printer.addPrintingObject("Number", False, 9)
        printer.addPrintingObject("Mail", True, 30)
        printer.printHeader()

        for employee in self.employees: 
            print(printer.formatValue(0, employee.name)+
                  printer.formatValue(1, employee.cpf)+
                  printer.formatValue(2, employee.number)+
                  printer.formatValue(3, employee.mail))