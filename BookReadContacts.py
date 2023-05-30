import BookMessage
import BookAddContacts

class BookReadContacts:
    FILE_NAME = 'my_contact_list_1.1.txt'
    def __init__(self):
        self.contacts_read = {}
        self.msg = BookMessage
        self.add_contact = BookAddContacts

    def initialize_contact(self) -> None:
        try:
            self.import_contacts()
        except:
            self.create_file()


    def import_contacts(self):
        with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
            file_string = file.readlines()
            for string in file_string:
                string = string.strip()
                name, number = string.split(', ')
                self.read_contacts(name, number)

    def create_file(self) -> None:
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            return print(BookMessage.BookMessage.SUCCESS_CREATED)

    def read_contacts(self, name, number):
        self.contacts_read[name] = number
        self.add_contact.add_cont.dicts.update(self.contacts_read)

    def print_contacts(self):
        for key, value in self.add_contact.add_cont.dicts.items():
            print(key, value)

read = BookReadContacts()
read.__init__()