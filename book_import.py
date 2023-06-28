class BookImport:

    def __init__(self, contacts):
        self.contacts = contacts
        self.contacts_new = {}
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
                string = (file_string[i])
                i += 1
                string = string.strip()
                string = string.split(': ')
                list1 = string[1]
                list1 = list1.strip('\"')
                list1 = list1.split(', ')
                self.contacts_new[string[0]] = list1

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
        choice = input('Перезаписать - 1, Объединить - 2, Создать новые - 3: ')
        if choice == '1':
            self.overwrite_contact()
        elif choice == '2':
            self.join_contact()
        elif choice == '3':
            self.create_new_name()

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