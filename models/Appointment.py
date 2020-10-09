from enum import Enum


class Appointment:
    def __init__(self, date, dateHour, employee, customer, status, description):
        self.date = date
        self.dateHour = dateHour
        self.employee = employee
        self.customer = customer
        self.status = status
        self.description = description


class Status(Enum):
    SCHEDULED = 1
    COMPLETED = 2
    CANCELED = 3
