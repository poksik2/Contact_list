from book_message import BookMessage
from book_validator import BookValidator

class BookAddContacts:

    def __init__(self, contacts):
        self.contacts = contacts
        self.number_contacts = dict()
        self.message = BookMessage
        self.validate = BookValidator(self.contacts)

    def create_contact(self):
        name = self.__create_name()
        self.number_contacts['Number: ']  = self.__create_number()
        self.__add_contact(name)
        print(self.message.SUCCESS_ADD)

    def __create_name(self):
        while True:
            name = self.__enter_name()
            if self.validate.validate_name(name):
                return name

    def __enter_name(self):
        name = input(self.message.ENTER_NAME)
        return name

    def __create_number(self):
        while True:
            number = self.__enter_number()
            if self.validate.validate_number(number):
                return number

    def __enter_number(self):
        number = input(self.message.ENTER_NUMBER)
        return number

    def __add_contact(self, name):
        self.contacts = {name: self.number_contacts}
        self.contacts.update(self.contacts)
        print(self.contacts)


# add_cont = BookAddContacts()
