class ObjectToPrint:
    def __init__(self, Title, LeftAligment, Length):
        self.Title = Title
        self.LeftAligment = LeftAligment
        self.Length = Length


class Printer:
    def __init__(self):
        self.ObjectsToPrint = []

    def formatValue(self, column, value):
        item = self.ObjectsToPrint[column]
        strValue = str(value)
        
        if item.LeftAligment:
            result = strValue.ljust(item.Length )
        else:
            result = strValue.rjust(item.Length )

        return result + " "

    def addPrintingObject(self, Title, LeftAligment, Length):        
        self.ObjectsToPrint.append( ObjectToPrint( Title, LeftAligment, Length) )

    def printHeader(self):
        nCount = 0
        output = ""
        for ObjectToPrint in self.ObjectsToPrint: 
            output += self.formatValue(nCount, ObjectToPrint.Title )
            nCount += 1
        print(output)
        print("")
