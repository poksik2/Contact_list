# import BookMessage

import BookAddContacts


class BookWriteContacts:
    FILE_NAME = 'my_contact_list_1.1.txt'

    def __init__(self):
        self.contacts = {}
        self.add_contact = BookAddContacts

    def write_contacts(self):
        self.contacts.update(self.add_contact.add_cont.dicts)
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            for name, number in self.contacts.items():
                file.write(f'{name}, {number}\n')


write = BookWriteContacts()
write.__init__()
