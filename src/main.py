from models.Vehicle import *
from models.Person import *
from models.Task import *
from models.Service import *

car = Car("car", 1998, "abc", "fiat")
print(car.model)

employee = Employee("lucas", 123, 123, "gay@gay.gay")
print(employee.name)

task = Task()
status = Status(1)

print(status)