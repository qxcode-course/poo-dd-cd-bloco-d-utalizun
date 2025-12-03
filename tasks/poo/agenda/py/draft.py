
#classe Fone
class Fone:
    def __init__(self, id: str, number: str):
        self.__id: str = id
        self.__number: str = number

    def isValid(self) -> bool:
        return True
    
    def getId(self)->str:
        return self.__id
    
    def getNumber(self)->str:
        return self.__number
    
    def __str__(self):
        return f"{self.__id}:{self.__number}"  
#fim da classe fone

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

#classe Agenda
class Agenda:
    def __init__(self):
        self.__contacts: list[Contact] = []

    def PosByName(self, name):
        for i in range(len(self.__contacts)):
            if self.__contacts[i].getName() == name:
                return i
        return -1
    
    def addContact(self, name: str, fones: list[Fone]):
        contactIndex = self.PosByName(name)
        if contactIndex != -1:
            contact = self.__contacts[contactIndex]
            for fone in fones:
                contact.addFone(fone)
            return
        contact = Contact(name)
        for fone in fones:
            contact.addFone(fone)
        self.__contacts.append(contact)
    
    def getContacts(self, name: str) -> list[Contact]:
        return sorted(self.__contacts, key=lambda contact: contact.getName())
    
    def rmContact(self, name: str):
        index = self.PosByName(name)
        if index == -1:
            self.__contacts.pop(index)

    def search(self, pattern: str) -> list[Contact]:
        result = []
        for contact in self.getContacts():
            if pattern in str(contact):
                result.append("- "+ str(contact))
                return "\n".join(result)
            
    
    def getFavorite(self) -> list[Contact]:
        return
    
    def getContact(self, name: str) -> None:
        index = self.PosByName(name)
        if index == -1:
            return None
        return self.__contacts[index]
    
    def __str__(self):
        result = []
        for contact in self.getContact():
            mark = "@" if contact.isFavorited() else "- "
            result.append(mark + str(contact))
            return "\n".join(result)

    
def buildFoneStr(foneStr: str) -> Fone:
        id, number = foneStr.split(":")
        return Fone(id,number)

#fim da classe Agenda 

#main
def main():

    agenda: Agenda = Agenda()

    while True:
        line: str = input()
        args: list[str] = line.split(' ')
        print(f'${line}')

        if args[0] == "add":
            name = args[1]
            fones = []

            for i in range(2, len(args)):
                fone = buildFoneStr(args[i])
                fones.append(fone)

            agenda.addContact(name,fones)

        elif args[0] == "show":
            print(agenda)

        elif args[0] == "end":
            break
        elif args[0] == "rmFone":
            name = args[1]
            index = int(args[2])
            contact = agenda.getContact(name)
            if contact:
                contact.rmFone(index)
            agenda.rmContact(name)
            agenda.addContact(contact.getName(), contact.getFones())

if __name__ == "__main__":
    main()
#fim da main