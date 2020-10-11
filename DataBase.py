from Printer import *
from ScheduleList import *

scheduleList = SchedulesList()


class DataBase(object):
    customers = []
    employees = []
    appointments = []
    idCounter = 0

    def findEmployee(self, employeeId):
        for employee in self.employees:
            if employee.id == employeeId:
                return employee
            else:
                print("Employee not found!")

    def findCustomer(self, customerCpf):
        for customer in self.customers:
            if customer.cpf == customerCpf:
                return customer
            else:
                print("Customer not found!")

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

    def freeSchedules(self, dateOfService):
        printer = Printer()
        printer.addPrintingObject("Option", True, 10)
        printer.addPrintingObject("Id", True, 10)
        printer.addPrintingObject("Name", True, 20)
        printer.addPrintingObject("Date", False, 15)
        printer.addPrintingObject("Hour", False, 10)
        printer.printHeader()

        appointmentListForThatDay = []
        for appointment in self.appointments:
            if appointment.date == dateOfService:
                appointmentListForThatDay.append(appointment)

        freeScheduleOption = 0
        freeSchedulesList = []
        for employee in self.employees:
            for hour in scheduleList.SCHEDULES:

                foundFreeHour = True
                for appointment in appointmentListForThatDay:
                    if appointment.employee == employee \
                            and appointment.dateHour == hour \
                            and appointment.dateHour + 1 == hour:
                        foundFreeHour = False

                if foundFreeHour:
                    freeScheduleOption += 1
                    freeSchedulesList.append(DataToMarkAppoint(freeScheduleOption, employee.id, employee.name,
                                                               dateOfService, hour))
        for x in freeSchedulesList:
            print(printer.formatValue(0, x.freeScheduleOption) +
                  printer.formatValue(1, x.employeeId) +
                  printer.formatValue(2, x.employeeName) +
                  printer.formatValue(3, x.dateOfService) +
                  printer.formatValue(4, x.hour))

        return freeSchedulesList

class DataToMarkAppoint:
    freeScheduleOption = None
    employeeId = None
    employeeName = None
    dateOfService = None
    hour = None

    def __init__(self, freeScheduleOption, employeeId, employeeName, dateOfService, hour):
        self.freeScheduleOption = freeScheduleOption
        self.employeeId = employeeId
        self.employeeName = employeeName
        self.dateOfService = dateOfService
        self.hour = hour





