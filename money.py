class Money:
    def __init__(self, Type = 'TL', Value = 0):
        self.__Type = Type
        self.__Value = Value

    def Value(self, Value):
        if Value>0:
            self.__Value = Value

    def __str__(self):
        return '%s, %s'%(self.__Type, self.__Value)

    def __repr__(self):
        return 'Money(%s)'%str(self)


D = Money('Dollar', 100)
D.__Type = 'Euro'
print(D.__repr__())