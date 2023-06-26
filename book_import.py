
class BookImport:

    def __init__(self, contacts):
        self.contacts = contacts
        self.contacts_new = dict()
        self.contact = dict()
        self.dict3 = dict()
        self.dict4 = dict()
    def initialization_contact(self):
        file_name = input('Enter file name: ')
        with open(file_name, 'r', encoding='utf-8') as file:
            file_string = file.readlines()
            #print(file_string)
            for string in file_string:
                string = string.strip()
                name, number = string.split(': ')
                self.contacts_new[name] = number


    def overlap_contacts(self):
        self.initialization_contact()
        for key, value in self.contacts.items():
            if key in self.contacts_new:
                self.dict3[key] = value
        #print(self.dict3, 1)
        for keys, values in self.contacts_new.items():
            if keys in self.contacts:
                self.dict4[keys] = values
        #print(self.dict4)
        for key, value in self.dict3.items():
            list1 = self.dict3[key]
            list1 = list1.strip('[]')
            list2 = self.dict4[key]
            #list2 = list2.strip('[]')
            list2 = list(list2)

            print(list2)

        self.print_contacts()

    def print_contacts(self):
        for key, value in self.contact.items():
            print(key, value)
