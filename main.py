#!/usr/bin/env python3
from DataBase import DataBase
from menuAppoitments import MenuAppoitments
from menuCustomer import MenuCustomer
from menuEmployee import MenuEmployee
import os

repository = DataBase()
clear = lambda: os.system('cls')

                
keep = True
while keep:
    clear()
    option = int(input("\nSelect the menu\n"
                       "1.Customer Management\n"
                       "2.Employee Management\n"
                       "3.Appointments Management\n"
                       "4.Quit\n"))

    if option == 1:
        menu = MenuCustomer(repository)
        menu.mainMenu()
    elif option == 2:        
        menu = MenuEmployee(repository)
        menu.mainMenu()
    elif option == 3:        
        menu = MenuAppoitments(repository)
        menu.mainMenu()
    elif option == 4:
        keep = False
