class ContactReader:
    # почитать про инкапсуляцию
    def __init__(self):
        self.contacts = {}
        self.__initialize_contact()

    def __initialize_contact(self):
        pass

    def print_contacts(self):
        pass


class ContactCreator:
    # выбери один из вариков: хранить в конструкторе контакты или передавать в метод create
    def __init__(self, contacts):
        self.contacts = contacts

    def create_contact(self, contacts):
        pass


class ContactDeleter:
    # выбери один из вариков: хранить в конструкторе контакты или передавать в метод delete
    def __init__(self, contacts):
        pass

    def delete_contact(self, contacts):
        pass


class ContactSaver:
    def save_contacts(self, contacts, file_path):
        pass


class MainContact:
    def __init__(self):
        self.reader = ContactReader()
        self.writer = ContactCreator(self.reader.contacts)
        self.deleter = ContactDeleter()
        self.saver = ContactSaver()

    def main(self):
        try:
            self.start_program()
        finally:
            self.saver.save_contacts()

    def start_program(self):
        while True:
            choise = input(self.msg.BookMessage.MENU)
            if choise == '1':
                self.reader.print_contacts()

            elif choise == '2':
                self.writer.create_contact()

            elif choise == '3':
                self.deleter.delete_contact()

            else:
                self.saver.save_contacts()
                exit()
