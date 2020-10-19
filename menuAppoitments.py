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
            
            for appointment in self.repository.appointments:
                if (cpf == appointment.customer.cpf )\
                        and (date == appointment.date) \
                        and (hour == appointment.dateHour):
                    found = True
                    actualAppoitment = appointment
            if not found:
                print("Appoitment not found")
                continue

            self.repository.appointments.remove(actualAppoitment)
            self.doAppointment()

    def mainMenu(self):
        option = int(input("Type the desired operation\n"
                        "1.Register appointment\n"
                        "2.Reeschedule appoitment\n"
                        "3.List\n"))

        if (option == 1):
            self.doAppointment()   
        if (option == 2):
            self.reescheduleAppoitment()
        if (option == 3):
            self.repository.listAppoitmentsByDate(input("Please, enter date in format dd/mm/yyyy\n"))
            input("")


    def askCustomerInfo(self):
        customersCPF = input("Please, enter customer's CPF:")
        customer = self.repository.findCustomer(customersCPF)
        if customer is None:
            print("Customer not registered")
            MenuCustomer = MenuCustomer(self.repository)
            MenuCustomer.registerCustomer()

        customer = self.repository.findCustomer(customersCPF)
        return customer


    def askTaskInfo(self):
        availableTasks = AvailableTask()
    # colocar avaible tasks no database
        availableTasks.getAllAvailableTasks()

        printer = Printer()

        printer.addPrintingObject("ID", True, 3)
        printer.addPrintingObject("Name", True, 30)
        printer.addPrintingObject("Description", True, 30)
        printer.printHeader()

        tasks = availableTasks.getAllAvailableTasks()

        for key in tasks:
            task = tasks[key]
            print(printer.formatValue(0,key) +
                printer.formatValue(1, task.name) +
                printer.formatValue(2, task.description))

        return availableTasks.getAvailableTask(int(input("Please enter task's ID: ")))

    def doAppointment(self):
        print("Scheduling a service")
        dateOfService = input("Which date to register appointment? Please, type in format dd/mm/yyyy\n")    
        customer = self.askCustomerInfo()
        selectedTask = self.askTaskInfo()    

        print("Free schedules per employee")
        freeScheduleList = self.repository.freeSchedules(dateOfService)

        chosenSchedule = int(input("Select the option that best fits: "))
        for options in freeScheduleList:
            if options.freeScheduleOption == chosenSchedule:
                appoitment = Appointment(options.dateOfService,
                                                        options.hour,
                                                        self.repository.findEmployee(
                                                            options.employeeId),
                                                        customer,
                                                        Status.SCHEDULED,
                                                        selectedTask
                                                        )
                break

        
        self.repository.appointments.append(appoitment)

        input("Operation finished:\nDate of service "+\
            dateOfService + " hour "+str(appoitment.dateHour)+".\n"+\
                "Employee: "+appoitment.employee.name+".\n"+\
                    "Task: "+appoitment.task.name+".")
