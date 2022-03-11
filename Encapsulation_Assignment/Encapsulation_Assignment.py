#create class
class Protected:
    def __init__(self):
        self._protectedVar = 0

#create object
obj = Protected()
obj._protectedVar= 324
#prints the object(protected)
print(obj._protectedVar)


#create class
class Private:
    def __init__(self):
        self.__privateVar = 15

    def getPrivate(self):
        print(self.__privateVar)

    def setPrivate(self, private):
        self.__privateVar = private

#create objects
obj = Private()
obj.getPrivate()    
obj.setPrivate(30)
obj.getPrivate()
