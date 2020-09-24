class _Person:
    def __init__(self, name, cpf, numer, mail):
        self.name = name
        self.cpf = cpf
        self.numer = numer
        self.mail = mail


class Employee(_Person):
    def __init__(self, name, cpf, numer, mail):
        super().__init__(name, cpf, numer, mail)


class Customer(_Person):
    def __init__(self, name, cpf, numer, mail, addres, birthDate, gender, civilState, isCustomerActive):
        super().__init__(name, cpf, numer, mail)
        self.addres = addres
        self.birthDate = birthDate
        self.gender = gender
        self.civilState = civilState
        self.isCustomerActive = isCustomerActive
