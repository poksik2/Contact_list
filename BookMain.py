from BookMessage import BookMessage
from BookReadContacts import BookReadContacts
from BookAddContacts import BookAddContacts
from BookWriteContacts import BookWriteContacts
from BookDeleteContacts import BookDeleteContacts
# читай про импорты


class MainContact:
    def __init__(self):
        self.contacts = {}
        self.message = BookMessage()
        self.reader = BookReadContacts()
        self.writer = BookAddContacts(self.contacts)
        self.deleter = BookDeleteContacts()
        self.saver = BookWriteContacts()

    def main(self):
        try:
            self.start_program()
        finally:
            self.exit_program()

    def start_program(self):
        self.reader.initialize_contact(self.contacts)
        while True:
            choice = input(self.message.MENU)
            if choice == '1':
                self.reader.print_contacts(self.contacts)

            elif choice == '2':
                self.writer.create_contact()

            elif choice == '3':
                self.deleter.remove_name(self.contacts)

            else:
                self.saver.save_contacts(self.contacts)
                exit()

    def exit_program(self):
        print(self.message.EXIT)
        exit()

start = MainContact()
start.main()
