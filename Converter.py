import json
class Convertor:
    def __init__(self):
        self.list = []
        self.dict = {}

    def exports(self):
        exports = open('Contacts.txt', 'rb')
        self.list = exports.readline()
        exports.close()

    def imports(self):
        imports = open('Contacts.txt', 'wb')
        imports.writelines(self.list)
        imports.close()

    def convert_dict_to_list(self):
        self.list = json.dumps(self.dict, sort_keys=True)
        self.list = bytes(self.list, encoding='utf-8')
    def convert_list_to_dict(self):
        self.list = bytes(self.list)
        self.dict = json.loads(self.list)


