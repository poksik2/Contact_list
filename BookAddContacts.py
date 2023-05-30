import BookMessage
#import BookReadContacts

class BookAddContacts:

    def __init__(self):
        self.dicts = {}
        self.main = BookMessage
        #self.read = BookReadContacts
    def add_contacts(self):
        name = self.enter_name()
        name = self.validate_name(name)
        number = self.enter_number()
        self.add(name,number)


    def enter_name(self):
        name = input('Name ')
        return name

    def enter_number(self):
        number = input('Number ')
        return number


    def validate_name(self, name):
        if not name:
            self.empty_name()
            name = self.enter_name()
            return name
        else:
            self.match_name(name)
#Прот повторе имени предлагает создать новый или редактировать старый
#При выборе создать новый контакт перезаписывает уже имеющийся!!!???
            return name

    def empty_name(self):
        print('Not Name ')

    def match_name(self, name):
        print(self.dicts)
        if name in self.dicts:
            choise = input('Create new - 1, Edit - 2')
            self.choise(choise,name)
            return name

    def choise(self, choise,name):
        if choise == '1':
            name = self.enter_name()
            return name
        elif choise == "2":
            number = self.enter_number()
            self.add(name,number)

    def add(self,name ,number):
        self.dicts[name] = number

add_cont = BookAddContacts()
add_cont.__init__()

