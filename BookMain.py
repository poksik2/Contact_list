import BookMessage
import BookAddContacts
import BookReadContacts
import BookDeleteContacts
import BookWriteContacts


class BookMain:

    def __init__(self):
        self.contacts = {}
        self.msg = BookMessage
        self.read = BookReadContacts
        self.add_contact = BookAddContacts
        self.write_contact = BookWriteContacts
        self.delete_contact = BookDeleteContacts

    def main(self):
        self.read.read.initialize_contact()
        while True:
            choise = input('1 - Read, 2 - Write, 3 - Delete, Any key - Exit: ')
            if choise == '1':
                self.contacts = self.read.read.contacts_read
                self.read.read.print_contacts()

            elif choise == '2':
                self.add_contact.add_cont.add_contacts()
                self.contacts.update(self.add_contact.add_cont.dicts)

            elif choise == '3':
                self.delete_contact.delete_cnt.delete_contact()

            else:
                self.write_contact.write.write_contacts()
                exit()







start = BookMain()
start.main()
