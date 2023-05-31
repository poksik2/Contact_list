import BookMessage
import BookAddContacts

class BookDeleteContacts:

    def __init__(self):
        self.msg = BookMessage
        self.add_contact = BookAddContacts

    def delete_contact(self):
        del self.add_contact.add_cont.dicts[self.add_contact.add_cont.enter_name()]
        print(self.msg.BookMessage.DELETE_CONTACT)

delete_cnt = BookDeleteContacts()
delete_cnt.__init__()