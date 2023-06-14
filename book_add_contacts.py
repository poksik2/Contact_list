from book_message import BookMessage
from book_validator import BookValidator

class BookAddContacts:

    def __init__(self, contacts):
        self.contacts = contacts
        self.contact = dict()
        self.number_contacts = dict()
        self.message = BookMessage
        self.validate = BookValidator(self.contacts)

    def create_contact(self):
        name = self.__create_name()
        self.add_more_number()
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

    def add_more_number(self):
        i = 0
        while True:
            i += 1
            number = self.__create_number()
            choice = input('Добавить еще один номер 1- Да, 2- Нет ')
            self.number_contacts[f'Number {i} '] = number
            if choice == '1':
                continue
            else:
                break

    def __create_number(self):
        while True:
            number = self.__enter_number()
            if self.validate.validate_number(number):
                return number

    def __enter_number(self):
        number = input(self.message.ENTER_NUMBER)
        return number

    def __add_contact(self, name):
        self.contact = {name: self.number_contacts}
        self.contacts.update(self.contact)



# add_cont = BookAddContacts()
