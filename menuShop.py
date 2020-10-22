from ScheduleList import SchedulesList
from models.Appointment import Appointment, Status
from models.Task import Task, AvailableTask
from Printer import Printer

from menuCustomer import MenuCustomer


class MenuShop:
    def __init__(self, repository):
        self.repository = repository

    def mainMenu(self):
        try:
            option = int(input("Type the desired operation\n"
                                "1.Register new task\n"
                                "2.Update existing task\n"
                                "3.Delete specific task\n"
                                "4.List\n"))

            if (option == 1):
                self.registerTask()   
            if (option == 2):
                self.updateTask()
            if (option == 3):
                self.deleteTask()
            if (option == 4):
                self.lisTasks()
            else:
                print("Please enter a valid option! Returning to main menu!")
        except:
            print("Please enter a valid option! Returning to main menu!")

    def registerTask(self):
        print("Registering task")
        

        
    def updateTask(self):
        print("Updating task")
        

        
    def deleteTask(self):
        print("Deleting task")
        

        
    def lisTasks(self):
        print("Listing tasks")
        

        