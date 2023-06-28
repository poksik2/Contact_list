from book_message import BookMessage
from book_validator import BookValidator
from contact_creator import ContactCreator


class Contact:
    name = None
    current_number = None
    numbers = []


class BookAdderContacts:  # naming

    def __init__(self, contacts):
        self.contacts = contacts
        self.contact = dict()
        self.number_contacts = list()
        # self.contact_ = Contact()
        self.message = BookMessage  # naming
        self.validate = BookValidator(self.contacts)

    def create_contact(self):
        name = self.__create_name()
        numbers = self.__create_number()
        self.__add_contact(name)
        # self.__add_contact(self.contact_)
        print(self.message.SUCCESS_ADD)

    def __create_name(self):
        while True:
            name = self.__enter_name()
            if self.validate.validate_name(name):
                # self.contact_.name = name
                return name

    def __enter_name(self):
        name = input(self.message.ENTER_NAME)
        return name

    def __create_number(self):
        i = 0
        # numbers = []
        while True:
            # i += 1
            number = self.__enter_number()
            result = self.validate.validate_number(number, self.contacts)  # naming is_valid
            if result:
                self.number_contacts.append(number)
                result = self.add_more_number()
                if not result:
                    break
        # return numbers

    def __enter_number(self):
        number = input(self.message.ENTER_NUMBER)
        return number

    def add_more_number(self):
        choice = input('Добавить еще один номер 1- Да, 2- Нет ')
        if choice == '1':
            # self.__create_number()
            return True
        elif choice == '2':
            return False

    def __add_contact(self, name: str) -> None:  # __create_contact
        self.contact = {name: self.number_contacts}
        self.contacts.update(self.contact)

# add_cont = BookAddContacts()
