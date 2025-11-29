#classe contato
class Contact:
    def __init__(self, name: str):
        self.__name: str = name
        self.__favorited: bool = False
        self.__fones: list[Fone] 
    def addFone (self, id: str, number: str):
        return
    def rmFone(self, index: int):
        return
    def toogleFavorited(self):
        return 
    def isFavorited(self):
        return bool
    def getFones(self):
        return list[Fone]
    def getName(self)->str:
        return self.__name
    def setName(self, name: str):
        self.__name = name
    def __str__(self):
        return
#fim de contato

#classe Fone
class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number
    def isValid(self):
        return bool
    def getId():
        return str
    def getNumber(self):
        return str
    def __str__(self):
        return
#fim da classe fone

