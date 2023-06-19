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

    def validate_number(self, number):
        result = True
        if len(number) != 5:
            print(self.message.ERR_NUMBER_LEN)
            result = False
        return result

    def __validate_number_by_length(self):
        pass
        #!!!!!!!!


    def __validate_match_number(self, number, number_contacts):
        #naming!
        result = True
        for name, numbers in number_contacts.items():
        #for name in number_contacts:
            contact = number_contacts[name]
            #print(numbers, 11111)
            #print(contact)
            for value in contact.values():
                if number == value:
                    print('Этот номер уже добавлен к другому контакту')
                    result = False

        return result