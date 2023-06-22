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
                name, number = string.split(': ')
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
        self.__print_number(contacts)

    def __print_number(self,contacts):
        choice = input('Enter contact name: ')
        i = 0
        if choice in contacts:
            numbers = contacts[choice]
            numbers = numbers.strip('[, ]')
            #numbers = numbers.strip(', ')
            numbers = numbers.split(', ')
            print((numbers))
            while i != len(numbers):
                print(f'ID {i+1}: {numbers[i]}')
                i += 1
        else:
            print('There is no contact with that name!')


#read = BookReadContacts()
