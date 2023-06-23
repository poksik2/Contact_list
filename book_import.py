
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
            for string in file_string:
                string = string.strip()
                name, number = string.split(': ')
                contact = {name: number}
                self.contacts_new.update(contact)

    def overlap_contacts(self):
        #global list1, listing, list2
        self.initialization_contact()
        for key, value in self.contacts.items():
            if key in self.contacts_new:
                self.dict3[key] = value
                print(self.dict3)
        for keys, values in self.contacts_new.items():
            if keys in self.contacts.items():
                self.dict4[keys] = values
                print(self.dict4)

        #for key, value in self.dict3.items():
            #list1 = list(set(self.dict3[key] + self.dict4[key]))
            #self.contacts[key] = list1
            # print(key,list1)
                #self.contact[name] = (listing)
            #print(self.contact)
        self.print_contacts()

    def print_contacts(self):
        for key, value in self.contact.items():
            print(key, value)
