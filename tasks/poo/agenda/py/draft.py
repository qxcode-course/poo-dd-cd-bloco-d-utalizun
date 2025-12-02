#classe contato
class Contact:
    def __init__(self, name: str):
        self.__name: str = name
        self.__favorited: bool = False
        self.__fones: list[Fone] = []

    def addFone (self, fone: Fone):
        self.__fones.append(fone)
    
    def rmFone(self, index: int):
        if 0 <= index < len(self.__fones):
            self.__fones.pop(index)
    
    def toogleFavorited(self):
        self.__favorited = not self.__favorited
    
    def isFavorited(self) -> bool:
        return self.__favorited
    
    def getFones(self):
        return self.__fones
    
    def getName(self) -> str:
        return self.__name
    
    def setName(self, name: str):
        self.__name = name

    def __str__(self):
        foneStrList = [str(fone) for fone in self.__fones]
        return f"{self.__name} [{", ".join(foneStrList)}]"
    
#fim de contato

#classe Fone
class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number
    def isValid(self) -> bool:
        return True
    def getId() -> str:
        return self.__id
    def getNumber(self)->str:
        return self.__number
    def __str__(self):
        return f"{self.__id}:{self.__number}"
#fim da classe fone

#classe Agenda
class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []

    def _PosByName(self, name):
        for i in range(len(self.__contacts)):
            if self.__contacts[i].getName() == name:
                return i
        return -1
    
    def __str__(self):
        result = []
        for contact in self.getContact():
            mark = "@" if contact.isFavorited() else "- "
            result.append(mark + str(contact))
            return "\n".join(result)

    def addContact(self, name: str, fones: list[Fone]):
        return
    
    def getContact(self, name: str) -> list[Contact]:
        return sorted(self.__contacts, key=lambda contact: contact.getName())
    
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