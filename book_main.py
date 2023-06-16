from book_message import BookMessage
from book_read_contacts import BookReaderContacts
from book_add_contacts import BookAdderContacts
from book_write_contacts import BookWriterContacts
from book_delete_contacts import BookDeleteContacts


class MainContact:
    # все классы назвать как существительные +!
    # проверка на уникальность по номеру и по имени (нельзя создать контакт если есть такое имя или есть такой номер) +!
    # множества и их методы - почитать +!
    # несколько номеров к одному контакту +!
    # валидатор в отдельный класс +!
    # импорт контактов из указанного файла (прибавить к своим контактам, исключить повторение имен) +!

    def __init__(self):
        self.contacts = dict()
        self.message = BookMessage()
        self.reader = BookReaderContacts()
        self.writer = BookAdderContacts(self.contacts)
        self.deleter = BookDeleteContacts()
        self.saver = BookWriterContacts()

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
                self.deleter.delete_contact(self.contacts)

            elif choice == '4':
                self.reader.import_more_contacts(self.contacts)

            else:
                self.saver.save_contacts(self.contacts)
                exit()

    def exit_program(self):
        print(self.message.EXIT)
        exit()


start = MainContact()
start.main()
