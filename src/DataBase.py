from models.Person import *

def singleton(cls, *args, **kw):
    instances = {}
    def _singleton():
       if cls not in instances:
            instances[cls] = cls(*args, **kw)
       return instances[cls]
    return _singleton

@singleton
class DataBase(object):
    a = 1
    empregados = [
        Employee("Lucas", "12345678951", 44449874, "lucas.cschuler@gmail.com"),
        Employee("Lucas", "12345678951", 44449874, "lucas.cschuler@gmail.com")
    ]

    def __init__(self, x=0):
        self.x = x        

    def appoitmentsByDay(day):
        return 