class Test():
    def __init__(self, arg1:int, arg2:int):
        self.__arg1 = arg1
        self.__arg2 = arg2

    @property
    def arg1(self):
        return self.__arg1
    
    @property
    def arg2(self):
        return self.__arg2