class BookImport:

    def __init__(self, contacts):
        self.contacts = contacts
        self.contacts_new = {}
        self.contact = dict()
        self.dict3 = dict()
        self.dict4 = dict()
        self.list1 = []

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

    def overlap_contacts(self):
        self.initialization_contact()
        for key, value in self.contacts.items():
            if key in self.contacts_new:
                self.dict3[key] = value
        for keys, values in self.contacts_new.items():
            if keys in self.contacts:
                self.dict4[keys] = values
        self.print_contacts()

    def print_contacts(self):
        for key, value in sorted(self.dict3.items()):
            print(key)
            print(self.dict3[key])
            print(self.dict4[key])