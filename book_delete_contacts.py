from book_message import BookMessage


class BookDeleterContacts:

    def __init__(self):
        self.message = BookMessage()

    def delete_contact(self, contacts):
        while True:
            name = self.enter_name()
            if self.validate_name(name, contacts):
                self.__delete_contact(name, contacts)
                break

    def enter_name(self):
        name = input(self.message.ENTER_NAME)
        return name

    def validate_name(self, name, contacts):
        if name not in contacts:
            print(self.message.NO_CONTACT)
        else:
            return name

    def __delete_contact(self, name, contacts):
        del contacts[name]
        print(self.message.DELETE_CONTACT)

# delete_cnt = BookDeleteContacts()
