class BookWriterContacts:
    FILE_NAME = 'my_contact_list_1.1.txt'

    def __init__(self):
        pass

    def save_contacts(self, contacts):
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            i = 0
            for name, number in contacts.items():
                number = str(number)
                number = number.strip('[]')
                print(type(number),number)
                file.write(f'{name}: {number}\n')
                i+=1

    def validate_contacts_for_saving(self):
        pass

# write = BookWriteContacts()
