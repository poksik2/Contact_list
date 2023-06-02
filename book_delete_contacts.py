from book_message import BookMessage


class BookDeleteContacts:

    def __init__(self):
        self.message = BookMessage()

    def remove_name(self, contacts):
        name = input(self.message.ENTER_NAME)
        self.validate_name(name, contacts)
        self.delete_contact(name, contacts)
        return name

    def validate_name(self, name, contacts):
        if name not in contacts:
            print('Нет контакта с таким именем')
        else:
            return

    def delete_contact(self, name, contacts):
        del contacts[name]
        print(self.message.DELETE_CONTACT)

#delete_cnt = BookDeleteContacts()
