from Printer import *
from ScheduleList import *

scheduleList = SchedulesList()


class DataBase(object):
    customers = []
    employees = []
    appointments = []
    idCounter = 0

    def deleteAppointment(self, customerCpf, date, hour):
        newAppointmentLister = []

        for appointment in self.appointments:
            if (customerCpf == appointment.customer.cpf) \
                    and (date == appointment.date) \
                    and (hour == appointment.dateHour):
                print("Deleting appointment corresponding to CPF " + customerCpf + " date " + date + " hour " +
                      str(hour))
            else:
                newAppointmentLister.append(appointment)

        self.appointments = newAppointmentLister

    def findAppointment(self, customerCpf, date, hour):
        actualAppointment = None
        found = False

        for appointment in self.appointments:
            if (customerCpf == appointment.customer.cpf) \
                    and (date == appointment.date) \
                    and (hour == appointment.dateHour):
                found = True
                actualAppointment = appointment
        if not found:
            print("Appointment not found")

        return actualAppointment

    def findEmployee(self, employeeId):
        for employee in self.employees:
            if employee.id == employeeId:
                return employee
            else:
                print("Employee not found!")

    def findEmployee(self, employeeCpf):
        for employee in self.employees:
            if employee.cpf == employeeCpf:
                return employee
            else:
                print("Employee not found!")

    def deleteEmployee(self, employeeCpf):
        newEmployeeList = []

        for employee in self.employees:
            if employee.cpf == employeeCpf:
                print("Deleting employee corresponding to CPF " + employee.cpf)
            else:
                newEmployeeList.append(employee)

        self.employees = newEmployeeList

    def findCustomer(self, customerCpf):
        for customer in self.customers:
            if customer.cpf == customerCpf:
                return customer
            else:
                print("Customer not found!")

    def registerCustomer(self, customer):
        self.customers.append(customer)

    def deleteCustomer(self, customerCpf):
        newCustomerLister = []

        for customer in self.customers:
            if customer.cpf == customerCpf:
                print("Deleting customer corresponding to CPF " + customerCpf)
            else:
                newCustomerLister.append(customer)

        self.customers = newCustomerLister

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

    def listAppoitmentsByDate(self, date):

        printer = Printer()

        appointmentListForThatDay = []
        for appointment in self.appointments:
            if appointment.date == date:
                appointmentListForThatDay.append(appointment)

        printer.addPrintingObject("Date", True, 10)
        printer.addPrintingObject("Hour", True, 4)
        printer.addPrintingObject("Employee's name", True, 25)
        printer.addPrintingObject("Customers's name", True, 25)
        printer.addPrintingObject("Status", True, 25)
        printer.addPrintingObject("Task", True, 25)
        printer.printHeader()

        for appointment in appointmentListForThatDay:
            print(printer.formatValue(0, appointment.date) +
                  printer.formatValue(1, appointment.dateHour) +
                  printer.formatValue(2, appointment.employee.name) +
                  printer.formatValue(3, appointment.customer.name) +
                  printer.formatValue(4, appointment.status) +
                  printer.formatValue(5, appointment.task.name))

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
                    if appointment.employee.id == employee.id \
                            and (appointment.dateHour == hour \
                                 or appointment.dateHour + 1 == hour \
                                 or appointment.dateHour - 1 == hour):
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
