from ScheduleList import SchedulesList
from models.Appointment import Appointment, Status
from models.Task import Task, AvailableTask
from Printer import Printer
from menuCustomer import MenuCustomer


class MenuAppoitments:
    def __init__(self, repository):
        self.repository = repository

    def reescheduleAppoitment(self):
        print("Enter appointment information")
        found = False
        while not found:
            cpf = input("Enter customer CPF: ")
            date = input("Enter appoitment date, in format dd/mm/yyyy: ")
            hour = int(input("Enter appoitment hour: "))
            actualAppointment = None
            
            for appointment in self.repository.appointments:
                if (cpf == appointment.customer.cpf )\
                        and (date == appointment.date) \
                        and (hour == appointment.dateHour):
                    found = True
                    actualAppointment = appointment
            if not found:
                print("Appoitment not found")
                continue

            self.repository.appointments.remove(actualAppointment)
            self.doAppointment()

    def mainMenu(self):
        try:
            option = int(input("Type the desired operation\n"
                                "1.Register appointment\n"
                                "2.Reeschedule\n"
                                "3.Delete an appoitment\n"
                                "4.List\n"))

            if (option == 1):
                self.doAppointment()   
            if (option == 2):
                self.reescheduleAppoitment()
            if (option == 3):
                self.deleteAppointment()
            if (option == 4):
                self.menuLists()
            else:
                print("Please enter a valid option! Returning to main menu!")
        except:
            print("Please enter a valid option! Returning to main menu! **Exception")

    def deleteAppointment(self):
        print("Enter appointment information")
        cpf = input("Enter customer CPF: ")
        date = input("Enter appoitment date, in format dd/mm/yyyy: ")
        hour = int(input("Enter appoitment hour: "))

        areYouSure = int(input("ARE YOU SURE YOU WANT TO DELETE APPOINTMENT? \n1. Yes\n2. No\n")) == 1
        if areYouSure:
            self.repository.deleteAppointment(cpf, date, hour)
        else:
            print("Ok, cancelling operation!")

    def listAppoitmentByCustomer(self):
        customer = self.askCustomerInfo(False)
        while (customer == None):
            customer = self.askCustomerInfo(False)
        
        clientAppoitments = [n for n in self.repository.appointments if n.customer.cpf == customer.cpf]

        order = int(input("Enter the order for the report\n1.Task code\n2.Date\n3.Task name\n"))

        if (order == 1):
            sortedAppoitments = sorted(clientAppoitments, key=lambda x: x.task.code, reverse=False)
        elif (order == 2):
            sortedAppoitments = sorted(clientAppoitments, key=lambda x:  x.date, reverse=False)
        elif (order == 3):
            sortedAppoitments = sorted(clientAppoitments, key=lambda x: x.task.name, reverse=False)

        printer = Printer()    

        printer.addPrintingObject("Date", True, 10)
        printer.addPrintingObject("Hour", True, 4)
        printer.addPrintingObject("Employee's name", True, 25)
        printer.addPrintingObject("Customers's name", True, 25)
        printer.addPrintingObject("Vehicle's model", True, 25)
        printer.addPrintingObject("Status", True, 25)        
        printer.addPrintingObject("Task", True, 25)
        printer.printHeader()

        for appointment in sortedAppoitments:
                print(printer.formatValue(0, appointment.date) +
                      printer.formatValue(1, appointment.dateHour) +
                      printer.formatValue(2, appointment.employee.name) +
                      printer.formatValue(3, appointment.customer.name) +
                      printer.formatValue(4, appointment.vehicle.model) +
                      printer.formatValue(5, appointment.status) +
                      printer.formatValue(6, appointment.task.name))  
        ##mover esse c�digo para a classe DataBase

    def menuLists(self):
        option = int(input("Which report?\n1.Appoitments by date\n2.Appoitments by customer\n"))

        if(option == 1):
            self.repository.listAppoitmentsByDate(input("Please, enter date in format dd/mm/yyyy\n"))
        if(option == 2):
            self.listAppoitmentByCustomer()
            
        input("")

    def askCustomerInfo(self, registerNewCustomer):
        customersCPF = input("Please, enter customer's CPF:")
        customer = self.repository.findCustomer(customersCPF)
        if customer is None:
            print("Customer not registered")
            if registerNewCustomer == True:
                menuCustomer = MenuCustomer(self.repository)
                customer = menuCustomer.registerCustomer()
            else: 
                return

        return customer


    def askTaskInfo(self):
        availableTasks = AvailableTask()
        availableTasks.getAllAvailableTasks()

        print("Select task to be executed: ")
        printer = Printer()
        printer.addPrintingObject("ID", True, 3)
        printer.addPrintingObject("Name", True, 30)
        printer.addPrintingObject("Description", True, 30)
        printer.printHeader()

        tasks = availableTasks.getAllAvailableTasks()

        for key in tasks:
            task = tasks[key]
            print(printer.formatValue(0, key) +
                  printer.formatValue(1, task.name) +
                  printer.formatValue(2, task.description))

        return availableTasks.getAvailableTask(int(input("Please enter task's ID: ")))

    def doAppointment(self):
        print("Scheduling a service")
        dateOfService = input("Which date to register appointment? Please, type in format dd/mm/yyyy\n")    
        
        customer = self.askCustomerInfo(True)
        vehicle = self.repository.findVehicleByCustomerCpf(customer.cpf)

        if vehicle == None:
            print("Vehicle not found for this customer, you will now be prompted to register a vehicle for this customer")
            menuCustomer = MenuCustomer(self.repository)
            vehicle = menuCustomer.registerVehicleForCustomer(customer)

        selectedTask = self.askTaskInfo()    

        print("Free schedules per employee")
        freeScheduleList = self.repository.freeSchedules(dateOfService)

        chosenSchedule = int(input("Select the option that best fits: "))
        for options in freeScheduleList:
            if options.freeScheduleOption == chosenSchedule:
                appoitment = Appointment(options.dateOfService,
                                                        options.hour,
                                                        self.repository.findEmployeeById(
                                                            options.employeeId),
                                                        customer,
                                                        vehicle,
                                                        Status.SCHEDULED,
                                                        selectedTask
                                                        )
                break

        
        self.repository.appointments.append(appoitment)

        input("Operation finished:\nDate of service "+\
            dateOfService + " hour "+str(appoitment.dateHour)+".\n"+\
                "Employee: "+appoitment.employee.name+".\n"+\
                    "Task: "+appoitment.task.name+".")
