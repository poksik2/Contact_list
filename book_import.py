class BookImport:

    def __init__(self, contacts):
        self.contacts = contacts
        self.contacts_new = dict()
        self.contact = dict()
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
        self.initialization_contact()
        for name, num in self.contacts.items():
            if name in self.contacts_new.keys() and self.contacts.keys():
                list1 = num
                list1 = eval(list1)
                print(type(list1))
        for name, num in self.contacts_new.items():
            if name in self.contacts.keys() and self.contacts_new.keys():
                list2 = (num)
                list2 = eval(list2)
                listing = list2 + list1
                #print(list(set(listing)))
        self.contact[name] = (list(set(listing)))
        print(self.contact)

