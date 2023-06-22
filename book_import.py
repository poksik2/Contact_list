
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
                list1=(num)
                print(num)
                list1 = list1.strip('[]')
                list1 = list1.split(', ')
                #print((list1))
            for names, nums in self.contacts_new.items():
                if names in self.contacts.keys() and self.contacts_new.keys():
                    list2=(nums)
                    print(nums)
                    list2 = list2.strip('[]')
                    list2 = list2.split(', ')
                    listing = list2 + list1
                    #print((listing))
                    self.contact[name] = (list(set(list1)),list(set(list2)) )
            #print(self.contact)
        #self.print_contacts()

    def print_contacts(self):
        for key, value in self.contact.items():
            print(key, value)
