from DataBase import DataBase
from menuAppoitments import MenuAppoitments
from menuCustomer import MenuCustomer
from menuEmployee import MenuEmployee
import os

class Menu:    
    def __init__(self):
        self.repository = DataBase()

    def clear(self):
        os.system('cls') 

    def main(self):       
        keep = True
        while keep:
            self.clear()
            try:
                option = int(input("\nSelect the menu\n"
                                "1.Customer Management\n"
                                "2.Employee Management\n"
                                "3.Appointments Management\n"
                                "4.Quit\n"))
                if option == 1:
                    menu = MenuCustomer(self.repository)
                    menu.mainMenu()
                elif option == 2:        
                    menu = MenuEmployee(self.repository)
                    menu.mainMenu()
                elif option == 3:        
                    menu = MenuAppoitments(self.repository)
                    menu.mainMenu()
                elif option == 4:
                    keep = False
                else:
                    print("Please enter a valid option!!!")
            except: 
                print("Please enter a valid option!!!")
