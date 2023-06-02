
class BookWriteContacts:
    FILE_NAME = 'my_contact_list_1.1.txt'

    def __init__(self):
        pass

    def save_contacts(self, contacts):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            for name, number in contacts.items():
                file.write(f'{name}, {number}\n')


#write = BookWriteContacts()
