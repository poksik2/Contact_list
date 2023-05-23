import json


class book:
    def __init__(self) -> None:
        self.list = []
        self.dict = {}

    def main(self):
        while True:
            choice = (input('Что будем делать? (Посмотреть - 1, Добавить - 2, Удалить - 3): '))  # вынеси в метод

            if choice == '1':
                self.reading()
            elif choice == '2':
                self.wtiting()
            elif choice == '3':
                self.dellite()
            else:
                break





    def wtiting(self) -> None:
        name = str(input())
        number = input()
        self.dict[name] = number
        self.convert_dict_to_list()
        self.imports()



    def reading(self) -> None:
        self.exports()
        self.listing()
    def dellite(self):
        self.exports()
        self.dell()
        self.imports()
        #self.list = json.dumps(self.keylist, sort_keys=True)
        #imports = open('3.txt', 'wb')
        #imports.write(bytes(self.list, encoding='utf-8'))
        #imports.close()


    def exports(self):
        exports = open('Contacts.txt', 'rb')
        self.list = exports.read()
        self.convert_list_to_dict()
        exports.close()


    def convert_dict_to_list(self):
        self.list = json.dumps(self.dict, sort_keys=True)
        self.list = bytes(self.list, encoding='utf-8')
    def imports(self):
        imports = open('Contacts.txt', 'wb')
        imports.write(self.list)
        imports.close()



    def convert_list_to_dict(self):
        self.list = bytes(self.list)
        self.dict = json.loads(self.list)

    def listing(self):
        for key, value in self.dict.items():
            print(key, ':', value)

    def dell(self):
        name = str(input())
        del self.dict[name]
        self.convert_dict_to_list()


my_list = book()
my_list.main()
