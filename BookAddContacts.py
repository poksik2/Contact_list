import BookMessage


# import BookReadContacts

class BookAddContacts:

    def __init__(self):
        self.dicts = {}
        self.msg = BookMessage
        # self.read = BookReadContacts

    def add_contacts(self):
        name = self.create_name()
        number = self.enter_number()
        number = self.validate_number(number)
        self.add(name, number)

    def create_name(self):
        name = self.enter_name()
        self.validate_name(name)
        return name

    def create_number(self):
        pass

    def enter_name(self):
        # !
        name = input(self.msg.BookMessage.ENTER_NAME)
        return name

    def validate_name(self, name):
        if not name:
            self.empty_name()
            self.create_name()

        elif name in self.dicts:
            # просто говорить что контакт с таким именем есть, введите новое имя
            choise = input(self.msg.BookMessage.OVERWRITE_NUMBER)
            name = self.choise(choise, name)

    def empty_name(self):
        print(self.msg.BookMessage.EMPTY_NAME)

    def match_name(self, name):
        if name in self.dicts:
            choise = input(self.msg.BookMessage.OVERWRITE_NUMBER)
            name = self.choise(choise, name)
            return name

    def choise(self, choise, name):
        if choise == '1':
            name = self.enter_name()
            return name
        elif choise == "2":
            return name

    def enter_number(self):
        number = input(self.msg.BookMessage.ENTER_NUMBER)
        return number

    def validate_number(self, number):
        if len(number) == 5:
            print(self.msg.BookMessage.SUCCESS_ADD)
            return number
        else:
            print(self.msg.BookMessage.ERR_NUMBER_LEN)
            number = self.enter_number()
            return number

    def add(self, name, number):
        self.dicts[name] = number


add_cont = BookAddContacts()
add_cont.__init__()
