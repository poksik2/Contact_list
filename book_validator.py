from book_message import BookMessage

class BookValidator:

    def __init__(self, contacts):
        self.contacts = contacts
        self.message = BookMessage


    def validate_name(self, name):
        if not name:
            print(self.message.EMPTY_NAME)
            return False

        elif name in self.contacts:
            print(self.message.OVERWRITE_NUMBER)
            return False
        return True

    def validate_number(self, number, contacts):
        result = self.__validate_number_by_length(number)
        if result == True:
            result = self.__validate_match_number(number,contacts)
        return result

    def __validate_number_by_length(self, number):
        result = True
        if len(number) != 5:
            print(self.message.ERR_NUMBER_LEN)
            result = False
        return result
        #!!!!!!!!


    def __validate_match_number(self, number, contacts):
        result = True
        for name in contacts:
            contact = contacts[name]
            if number in contact:
                print('Этот номер уже добавлен к другому контакту')
                result = False
        return result