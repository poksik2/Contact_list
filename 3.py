import json


class book:
    def __init__(self) -> None:
        self.list = []
        self.keylist = {}

    def main(self):
        while True:
            choice = (input('Что будем делать? (Посмотреть - 1, Добавить - 2): '))  # вынеси в метод

            if choice == '1':
                self.exports()
            elif choice == '2':
                self.inmport()
            else:
                break





    def inmport(self) -> None:

        name = str(input())
        number = input()

        self.keylist[name] = number
        self.list = json.dumps(self.keylist, sort_keys=True)
        imports = open('3.txt', 'wb')
        imports.write(self.list.encode('utf-8'))
        imports.close()
        print(type(self.list))
        print(self.list)


    def exports(self) -> None:
        exports = open('3.txt', 'r')
        self.list = exports.read()
        self.list = bytes(self.list, encoding='utf-8')
        self.keylist = json.loads(self.list)
        print(type(self.keylist))
        print(self.keylist)
        exports.close()


    #def dell(self):
        #name = str(input())
        #self.list = self.list.pop(name)


my_list = book()
my_list.main()