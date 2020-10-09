class Vehicle:
    def __init__(self, model, year, plate, manufacturer):
        self.model = model
        self.year = year
        self.plate = plate
        self.manufacturer = manufacturer


class Car(Vehicle):
    pass


class Motorcycle(Vehicle):
    pass
