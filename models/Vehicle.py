class Vehicle:
    def __init__(self, model, year, plate, manufacturer, owner):
        self.model = model
        self.year = year
        self.plate = plate
        self.manufacturer = manufacturer
        self.owner = owner


class Car(Vehicle):
    def __init__(self, model, year, plate, manufacturer, owner):
        super().__init__(model, year, plate, manufacturer, owner)


class Motorcycle(Vehicle):
    def __init__(self, model, year, plate, manufacturer, owner):
        super().__init__(model, year, plate, manufacturer, owner)
