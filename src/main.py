#!/usr/bin/env python3

from src.models.Vehicle import *
from src.models.Person import *
from src.models.Task import *
from src.models.Service import *

car = Car("car", 1998, "abc", "fiat")
print(car.model)

employee = Employee("lucas", 123, 123, "gay@gay.gay")
print(employee.name)

status = Status(1)

print(status)
