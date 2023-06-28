from book_validator import BookValidator
class BookEditorContacts:

    def __init__(self, contacts):
        self.contacts = contacts
        self.validator = BookValidator(self.contacts)

    def editor_contacts(self):
        while True:
            print('----РЕДАКТОР----')
            choice = input('Сменить имя - 1, Сменить номер - 2, Добавить номер - 3, Удалить номер - 4, Выход - Any key : ')
            if choice == '1':
                self.change_the_name()
            elif choice == '2':
                self.change_the_one_number()
            elif choice == '3':
                self.add_number_to_contact()
            elif choice == '4':
                self.remove_number_to_contact()
            else:
                break

    def change_the_name(self):
        self.print_contact()
        old_name = self.enter_old_name()
        new_name = self.enter_new_name()
        self.contacts[new_name] = self.contacts.pop(old_name)


    def enter_new_name(self):
        while True:
            new_name = input(f'Введите новое имя : ')
            if self.validator.validate_name(new_name):
                return new_name
    def change_the_one_number(self):
        self.print_contact()
        choice_name = self.print_number()
        choice_id = input('Enter ID: ')
        new_number = self.enter_new_number()
        numbers = self.contacts[choice_name]
        numbers[int(choice_id)-1] = new_number

    def add_number_to_contact(self):
        self.print_contact()
        choice = self.enter_old_name()
        new_number = self.enter_new_number()
        self.contacts[choice].append(new_number)

    def enter_old_name(self):
        while True:
            old_name = input('Enter name: ')
            if old_name not in self.contacts:
                continue
            else:
                return old_name

    def enter_new_number(self):
        while True:
            new_number = input('Enter new number: ')
            if self.validator.validate_number(new_number,self.contacts):
                return new_number

    def remove_number_to_contact(self):
        self.print_contact()
        choice_name = self.print_number()
        choice_id = input('Enter ID: ')
        numbers = self.contacts[choice_name]
        del numbers[int(choice_id)-1]

    def print_contact(self):
        for key, value in self.contacts.items():
            print(key)

    def print_number(self,):
        choice = input('Enter contact name: ')
        i = 0
        if choice in self.contacts:
            numbers = self.contacts[choice]
            while i != len(numbers):
                print(f'ID {i+1}: {numbers[i]}')
                i += 1
            return choice
        else:
            print('There is no contact with that name!')