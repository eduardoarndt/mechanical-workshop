#!/usr/bin/env python3
from DataBase import DataBase
from models.Person import Customer, Employee
from ScheduleList import SchedulesList
from models.Appointment import Appointment, Status
from models.Task import Task, AvailableTask

repository = DataBase()
scheduleList = SchedulesList()
ids = 0


def menuEmployee():
    option = int(input("Type the desired operation\n1.Register\n2.List\n"))

    if option == 1:
        registerEmployee()
    elif option == 2:
        repository.listEmployees()


def menuCustomer():
    option = int(input("Type the desired operation\n1.Register\n2.List\n"))

    if (option == 1):
        registerCustomer()
    elif option == 2:
        activeCustomerOption = int(input("Which customers to list?\n1.Actives\n2.Inactives\n"))
        repository.listCustomers(activeCustomerOption == 1)


def registerCustomer():
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

    repository.customers.append(newCustomer)


def registerEmployee():
    employeeName = input('Enter employee''s name: ')
    employeeCpf = input('Enter employee''s CPF: ')
    employeeNumber = input('Enter employee''s number: ')
    employeeEmail = input('Enter employee''s email: ')

    repository.idCounter += 1
    newEmployee = Employee(employeeName, employeeCpf, employeeNumber, employeeEmail, repository.idCounter)
    repository.employees.append(newEmployee)


def menuAppointments():
    option = int(input("Type the desired operation\n"
                       "1.Register appointment\n"
                       "2.List\n"))

    if (option == 1):
        dateOfService = input("Which date to register appointment? Please, type in format dd/mm/yy\n")
        retrieveEmployeeFreeSchedule(dateOfService)
        # percorrer os serviços que tem data = a que foi informada
        # vou anotar qual funcionário é e qual horário é

        # para cada funcionario
        # começa as 8h... quando chegar no horário de um serviço marcadp que eu tenho na lista, não printa
        # e segue


# mds esse código tá um horror
def retrieveEmployeeFreeSchedule(dateOfService):
    # perguntar qual cliente
    # salvar cpf to cliente

    # perguntar qual task
    availableTasks = AvailableTask()
    #print this, ask which
    availableTasks.getAllAvailableTasks()

    taskChosen = availableTasks.getAvailableTask(1)


    print("Free schedules per employee")
    freeScheduleList = repository.freeSchedules(dateOfService)

    chosenSchedule = int(input("Select the option that best fits"))
    for options in freeScheduleList:
        if options.freeScheduleOption == chosenSchedule:
            repository.appointments.append(Appointment(options.dateOfService,
                                                       options.hour,
                                                       repository.findEmployee(options.employeeId),
                                                       repository.findCustomer("CPF DO CUSTOMER"),
                                                       Status.SCHEDULED,
                                                       taskChosen
                                                       ))

    # should have one item if this worked!
    print(repository.appointments)


keep = True
while keep:
    option = int(input("\nSelect the menu\n"
                       "1.Customer Management\n"
                       "2.Employee Management\n"
                       "3.Appointments Management\n"
                       "4.Quit\n"))

    if option == 1:
        menuCustomer()
    elif option == 2:
        menuEmployee()
    elif option == 3:
        menuAppointments()
    elif option == 4:
        keep = False
