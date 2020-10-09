from Printer import *
from ScheduleList import *

scheduleList = SchedulesList()


class DataBase(object):
    customers = []
    employees = []
    appointments = []
    idCounter = 0

    def listCustomers(self, printOnlyActives):
        printer = Printer()

        printer.addPrintingObject("Name", True, 25)
        printer.addPrintingObject("CPF", True, 11)
        printer.addPrintingObject("Number", False, 9)
        printer.addPrintingObject("Mail", True, 25)
        printer.addPrintingObject("Address", True, 30)
        printer.addPrintingObject("Birth date", True, 10)
        printer.addPrintingObject("Gender", False, 10)
        printer.addPrintingObject("Civil State", False, 15)
        printer.printHeader()

        for customer in self.customers:
            if customer.isCustomerActive == printOnlyActives:
                print(printer.formatValue(0, customer.name) +
                      printer.formatValue(1, customer.cpf) +
                      printer.formatValue(2, customer.number) +
                      printer.formatValue(3, customer.mail) +
                      printer.formatValue(4, customer.address) +
                      printer.formatValue(5, customer.birthDate) +
                      printer.formatValue(6, customer.gender) +
                      printer.formatValue(7, customer.civilState))

    def listEmployees(self):
        printer = Printer()

        printer.addPrintingObject("Name", True, 25)
        printer.addPrintingObject("CPF", True, 11)
        printer.addPrintingObject("Number", False, 9)
        printer.addPrintingObject("Mail", True, 30)
        printer.printHeader()

        for employee in self.employees:
            print(printer.formatValue(0, employee.name) +
                  printer.formatValue(1, employee.cpf) +
                  printer.formatValue(2, employee.number) +
                  printer.formatValue(3, employee.mail))

    def freeSchedules(self):
        printer = Printer()
        printer.addPrintingObject("id", True, 10)
        printer.addPrintingObject("Name", True, 25)
        printer.addPrintingObject("Hour", True, 25)
        printer.printHeader()

        for employee in self.employees:
            for hour in scheduleList.SCHEDULES:

                foundFreeHour = False
                for appointment in self.appointments:
                    if appointment.employee == employee \
                            and appointment.dateHour == hour \
                            and appointment.dateHour + 1 == hour:
                        foundFreeHour = True

                if not foundFreeHour:
                    print(printer.formatValue(0, employee.id) +
                          printer.formatValue(0, employee.name) +
                          printer.formatValue(1, hour))
