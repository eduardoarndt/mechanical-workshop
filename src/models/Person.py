class _Person:
    def __init__(self, name, cpf, number, mail):
        self.name = name
        self.cpf = cpf
        self.number = number
        self.mail = mail


class Employee(_Person):
    def __init__(self, name, cpf, number, mail):
        super().__init__(name, cpf, number, mail)


class Customer(_Person):
    def __init__(self, name, cpf, number, mail, address, birthDate, gender, civilState, isCustomerActive):
        super().__init__(name, cpf, number, mail)
        self.address = address
        self.birthDate = birthDate
        self.gender = gender
        self.civilState = civilState
        self.isCustomerActive = isCustomerActive
