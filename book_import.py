class BookImport:

    def __init__(self, contacts):
        self.contacts = contacts
        self.contacts_new = {}
        # naming
        self.dict3 = dict()
        self.dict4 = dict()
        self.list1 = []

    def overlap_contacts(self):
        self.initialization_contact()
        self.repeat_old_contacts()
        self.repeat_new_contacts()
        self.print_contacts()
        self.choice_action()

    def initialization_contact(self):
        file_name = 'my_contacts.txt'
        with open(file_name, 'r', encoding='utf-8') as file:
            file_string = file.readlines()
            i = 0
            while i != len(file_string):
                # naming
                string = (file_string[i])
                i += 1
                string = string.strip()
                string = string.split(': ')
                # name = string[0]
                # numbers = string[1]
                # self.parse_phone_number_sting(numbers)
                list1 = string[1]
                list1 = list1.strip('\"')
                list1 = list1.split(', ')
                self.contacts_new[string[0]] = list1

    def parse_phone_number_sting(self, number_string):
        string_without_bracers = number_string[1:-1]
        numbers_as_string = string_without_bracers.split(',')
        numbers = [self.strip_number_string(number_string) for number_string in numbers_as_string]
        return numbers

    def strip_number_string(self, number_string: str) -> int:
        digital_string = ''.join([symbol for symbol in number_string if symbol.isdigit()])
        return int(digital_string)

    def repeat_old_contacts(self):
        for key, value in self.contacts.items():
            if key in self.contacts_new:
                self.dict3[key] = value

    def repeat_new_contacts(self):
        for keys, values in self.contacts_new.items():
            if keys in self.contacts:
                self.dict4[keys] = values

    def print_contacts(self):
        for key, value in sorted(self.dict3.items()):
            print(key)
            print(self.dict3[key])
            print(self.dict4[key])

    def choice_action(self):
        # при импорте возникли неполадки
        # имена дубликаты: имя1, имя2

        # что делать с номерами контакта имя1?

        # что делать с номерами контакта имя2?

        choice = input('Перезаписать - 1, Объединить - 2, Создать новый контакт - 3: ')
        if choice == '1':
            self.overwrite_contact()
        elif choice == '2':
            self.join_contact()
        elif choice == '3':
            self.create_new_name()
        # пропустить
        # пропустить все

    def overwrite_contact(self):
        self.contacts |= self.dict4

    def join_contact(self):
        for key, value in self.dict3.items():
            all_number = list(set(self.dict3[key] + self.dict4[key]))
            self.contacts[key] = all_number

    def create_new_name(self):
        for name, value in self.dict3.items():
            new_name = input(f'Введите новое имя для контакта {name}: ')
            self.dict4[new_name] = self.dict4.pop(name)
        self.contacts |= self.dict4
