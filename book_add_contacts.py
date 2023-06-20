from book_message import BookMessage
from book_validator import BookValidator

class BookAdderContacts:

    def __init__(self, contacts):
        self.contacts = contacts
        self.contact = dict()
        self.number_contacts = list()
        self.message = BookMessage
        self.validate = BookValidator(self.contacts)

    def create_contact(self):
        name = self.__create_name()
        self.__create_number()
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
            choice = input('Добавить еще один номер 1- Да, 2- Нет ')
            if choice == '1':
                return True
            elif choice == '2':
                return False
    def __create_number(self):
        i = 0
        while True:
            i += 1
            number = self.__enter_number()
            print(self.number_contacts)
            result = self.validate.validate_number(number, self.contacts)
            if result == True:
                self.number_contacts.append(number)
                result = self.add_more_number()
                if result == False:
                    break

    def __enter_number(self):
        number = input(self.message.ENTER_NUMBER)
        return number

    def __add_contact(self, name):
        self.contact = {name: self.number_contacts}
        self.contacts.update(self.contact)

# add_cont = BookAddContacts()
