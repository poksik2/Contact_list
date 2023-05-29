import BookMessage
import BookAddContacts
import BookReadContacts
# import BookDeleteContacts
import BookWriteContacts


class BookMain:

    def __init__(self):
        self.contacts = {}
        self.msg = BookMessage
        self.read = BookReadContacts
        self.add_contact = BookAddContacts
        self.write_contact = BookWriteContacts

    def main(self):
        while True:
            choise = input('1 - Read, 2 - Write : ')
            if choise == '1':
                self.contacts = self.read.read.contacts_read
                self.read.read.print_contacts()
            elif choise == '2':
                self.contacts.update(self.add_contact.add_cont.dicts)
                self.write_contact.write.write_contacts()


start = BookMain()
start.main()
