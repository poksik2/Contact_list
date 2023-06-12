from book_message import BookMessage


class BookAddContacts:

    def __init__(self, contacts):
        self.contacts = contacts
        self.message = BookMessage

    def create_contact(self):
        name = self.__create_name()
        number = self.__create_number()
        self.__add_contact(name, number)
        print(self.message.SUCCESS_ADD)

    def __create_name(self):
        while True:
            name = self.__enter_name()
            if self.is_valid_name(name):
                return name

    def __enter_name(self):
        name = input(self.message.ENTER_NAME)
        return name

    def is_valid_name(self, name):
        if not name:
            print(self.message.EMPTY_NAME)
            return False

        elif name in self.contacts:
            print(self.message.OVERWRITE_NUMBER)
            return False
        return True

    def __create_number(self):
        while True:
            number = self.__enter_number()
            if self.is_valid_number(number):
                return number

    def __enter_number(self):
        number = input(self.message.ENTER_NUMBER)
        return number

    def is_valid_number(self, number):
        result = True
        if len(number) != 5:
            print(self.message.ERR_NUMBER_LEN)
            result = False
        return result

    def __add_contact(self, name, number):
        self.contacts[name] = number

# add_cont = BookAddContacts()
