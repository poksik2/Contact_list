from book_message import BookMessage


class BookReaderContacts:
    FILE_NAME = 'my_contact_list_1.1.txt'

    def __init__(self):
        self.message = BookMessage()

    def initialize_contact(self, contacts):
        try:
            contacts = self.import_contacts(contacts)
            return contacts
        except:
            self.create_file()

    def import_contacts(self, contacts):
        with open(self.FILE_NAME, 'r', encoding='utf-8') as file:
            file_string = file.readlines()
            for string in file_string:
                string = string.strip()
                name, number = string.split('; ')
                number = eval(number)
                contact = {name: number}
                contacts.update(contact)
            return contacts

    def create_file(self) -> None:
        with open(self.FILE_NAME, 'w', encoding='utf-8') as file:
            return print(self.message.SUCCESS_CREATED)

    def print_contacts(self, contacts):
        print(self.message.TITLE)
        for key, value in contacts.items():
            print(key)
            pass
        self.__print_number(contacts)

    def __print_number(self,contacts):
        choice = input('Enter contact name: ')
        if choice in contacts:
            numbers = contacts[choice]
            i = 0
            print(choice)
            for name, number in numbers.items():
                i += 1
                number = numbers[name]
                print(f'Nambers {i}: {number}')
        else:
            print('There is no contact with that name!')

    def import_more_contacts(self, contacts):
        file_name = input('Enter file name: ')
        with open(file_name, 'r', encoding='utf-8') as file:
            file_string = file.readlines()
            for string in file_string:
                string = string.strip()
                name, number = string.split('; ')
                number = eval(number)
                contact = {name: number}
                contacts.update(contact)
            return contacts

#read = BookReadContacts()
