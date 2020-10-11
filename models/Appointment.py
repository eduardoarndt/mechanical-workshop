from enum import Enum


class Appointment:
    def __init__(self, date, dateHour, employee, customer, status, task):
        self.date = date
        self.dateHour = dateHour
        self.employee = employee
        self.customer = customer
        self.status = status
        self.task = task


class Status(Enum):
    SCHEDULED = 1
    COMPLETED = 2
    CANCELED = 3
