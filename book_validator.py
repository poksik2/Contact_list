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

    def match_number(self, number, number_contacts):
        result = True
        for name, numbers in number_contacts.items():
            contact = number_contacts[name]
            #print(contact)
            for key, value in contact.items():
                value = contact[key]
                #print(value)
                if number == value:
                    #print(contact)
                    print('Этот номер уже добавлен к другому контакту')
                    result = False

                else:
                    break
        return result