class Task:
    def __init__(self, taskCode, taskName, taskDescription):
        self.code = taskCode
        self.name = taskName
        self.description = taskDescription


class AvailableTask:
    availableTask = None

    def __init__(self):
        self.availableTask = {
            # id: (name, description)
            1: ("Little Hammer of Gold", "We hammer your car till it looks like you never crashed it, dumb ass"),
            2: ("Jet Wax", "We clean your car till it looks like a mirror"),
            3: ("Checkup", "You don't understand about cars so you came to us, nice!")
        }

    def getAllAvailableTasks(self):
        return self.availableTask

    def getAvailableTask(self, id):
        if id in self.availableTask:
            return self.availableTask.get(id)
