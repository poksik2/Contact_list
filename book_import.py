
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
                #print(string)
                i += 1
                string = string.strip()
                #print(string)
                string = string.split(': ')
                #print(string)
                list1 = string[1]
                #print(list1)
                list1 = list1.split(', ')
                self.contacts_new[string[0]] = list1
            print(self.contacts_new)


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
