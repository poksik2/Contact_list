from book_message import BookMessage


class BookAddContacts:

    def __init__(self, contacts):
        self.contacts = contacts
        self.message = BookMessage

    def create_contact(self):
        name = self.create_name()
        number = self.create_number()
        self.add_contact(name, number)

    def create_name(self):
        name = self.enter_name()
        name = self.validate_name(name)
        return name

    def enter_name(self):
        name = input(self.message.ENTER_NAME)
        return name

    def validate_name(self, name):
        if not name:
            print(self.message.EMPTY_NAME)
            name = self.create_name()
            return name
        elif name in self.contacts:
            print(self.message.OVERWRITE_NUMBER)
            self.create_contact()
        else:
            return name

    def create_number(self):
        number = self.enter_number()
        number = self.validate_number(number)
        return number

    def enter_number(self):
        number = input(self.message.ENTER_NUMBER)
        return number

    def validate_number(self, number):
        if len(number) == 5:
            print(self.message.SUCCESS_ADD)
            return number
        else:
            print(self.message.ERR_NUMBER_LEN)
            number = self.create_number()
            return number

    def add_contact(self, name, number):
        self.contacts[name] = number


#add_cont = BookAddContacts()
