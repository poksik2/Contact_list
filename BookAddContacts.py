import BookMessage


class BookAddContacts:

    def __init__(self):
        self.dicts = {}
        self.main = BookMessage


    def enter_name(self) :
        name = input('Name ')
        return name

    def enter_number(self):
        number = input('Number ')
        return number

    def add_contacts(self):
        self.dicts[self.enter_name()] = self.enter_number()



add_cont = BookAddContacts()
add_cont.add_contacts()