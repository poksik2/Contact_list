import json
from typing import List, Any


class book:

    def main(self):
        while True:
            choice = (input('Что будем делать? (Посмотреть - 1, Добавить - 2): '))  # вынеси в метод

            if choice == '1':
                self.exports()
            elif choice == '2':
                self.inmport()
            else:
                break


    def __init__(self) -> None:
        self.list = []
        self.keylist = {}



    def inmport(self) -> None:


        name = str(input())
        number = input()

        self.keylist[name] = number
        self.list = json.dumps(self.keylist)
        #self.list = json.loads(self.list)




        imports = open('3.txt', 'wb')
        imports.writelines(self.list.encode())
        imports.close()


        #print(type(self.list))
        #print(type(self.keylist))
        #self.dell()
        #print(self.list)


    def exports(self) -> None:
        exports = open('3.txt', 'rb')


        self.list = exports.readline()

        #print(type(self.list))
        print(self.list)
        exports.close()


    #def dell(self):
        #name = str(input())
        #self.list = self.list.pop(name)


my_list = book()
my_list.main()