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

#classe Agenda
class Agenda:
    def __init__(self):
        self.__contacts:str = list[Contact]
    def _PosByName(self, name: str) -> int:
        return
    def __str__(self):
        return
    def addContact(self, name: str, fones: list[Fone]):
        return
    def getContact(self, name: str) -> Contact | None:
        return
    def rmContact(self, name: str):
        return
    def search(self, pattern: str) -> list[Contact]:
        return
    def getFavorite(self) -> list[Contact]:
        return
    def getContacts(self) -> list[Contact]:
        return
#fim da classe Agenda 

#main
def main():
    agenda: Agenda = Agenda()
    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'${line}')
    main()
#fim da main