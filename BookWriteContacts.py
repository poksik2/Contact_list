#import BookMessage
#import BookMain
import BookAddContacts

class BookWriteContacts:
    FILE_NAME = 'my_contact_list_1.1.txt'
    def __init__(self):
        self.contacts = {}
        #self.main = BookMain
        self.add_contact = BookAddContacts

    def write_contacts(self):
        self.contacts.update(self.add_contact.add_cont.dicts)
        #print(self.contacts)
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            for name, number in self.contacts.items():
                file.write(f'{name}, {number}\n')
                #file.writelines(f'{name}, {number} ')

write = BookWriteContacts()
write.__init__()
