class ObjectToPrint:
    def __init__(self, title, leftAligment, length):
        self.Title = title
        self.LeftAligment = leftAligment
        self.Length = length


class Printer:
    def __init__(self):
        self.objectsToPrint = []

    def formatValue(self, column, value):
        item = self.objectsToPrint[column]
        strValue = str(value)

        if item.LeftAligment:
            result = strValue.ljust(item.Length)
        else:
            result = strValue.rjust(item.Length)

        return result + " "

    def addPrintingObject(self, title, leftAligment, length):
        self.objectsToPrint.append(ObjectToPrint(title, leftAligment, length))

    def printHeader(self):
        nCount = 0
        output = ""
        for objectToPrint in self.objectsToPrint:
            output += self.formatValue(nCount, objectToPrint.Title)
            nCount += 1
        print(output)
        print("")
