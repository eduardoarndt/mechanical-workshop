class Task:
    def __init__(self, description, code):
        self.description = description
        self.code = code


class AvailableTask():
    def __init__(self, availableTask):
        self.availableTask = {
            Task("Martelinho de ouro", 1),
            Task("Chapeação", 2)
        }
