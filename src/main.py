#!/usr/bin/env python3
from DataBase import DataBase
from models.Person import *

repository = DataBase()

def menuEmployee():    
    opcao = int(input("Type the desired operation\n1.Register\n2.List\n"))
     
    if (opcao == 1):
        registerEmployee()
    elif opcao == 2:
        repository.listEmployees()

def menuCustomer():    
    opcao = int(input("Type the desired operation\n1.Register\n2.List\n"))
     
    if (opcao == 1):
        registerCustomer()
    elif opcao == 2:
        repository.listCustomers()

def registerCustomer():
    newCustomer = Customer('', '', 0, '', '', '', '', '', True)    
    newCustomer.name       = input('Enter customer''s name: ')    
    newCustomer.cpf        = input('Enter customer''s CPF: ')    
    newCustomer.number     = int(input('Enter customer''s number: '))
    newCustomer.address    = input('Enter customer''s address: ')    
    newCustomer.birthDate  = input('Enter customer''s birthDate: ')    
    newCustomer.gender     = input('Enter customer''s gender: ')
    newCustomer.civilState = input('Enter customer''s civilState: ')  

    repository.customers.append(newCustomer)

def registerEmployee():
    newEmployee = Employee('', '', 0, '')    
    newEmployee.name   = input('Enter customer''s name: ')    
    newEmployee.cpf    = input('Enter customer''s CPF: ')    
    newEmployee.number = int(input('Enter customer''s number: '))
    newEmployee.mail   = input('Enter customer''s email: ')    

    repository.employees.append(newEmployee)
keep = True
while (keep):
    opcao = int(input("'\nSelect the menu\n1.Customer\n2.Employee\n3.Quit\n"))
     
    if (opcao == 1):
        menuCustomer()
    elif opcao == 2:
        menuEmployee()
    elif opcao == 3:
        keep = False       
