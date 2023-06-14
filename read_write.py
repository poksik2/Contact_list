
class Test:

    def __init__(self):
        self.test_list = dict()
        self.num_list = dict()

    def add_to_list(self):
        #self.num_list = {'Vova': {'Number1: ': '4321', 'Number2 ': '1234'}}
        name = input('Name: ')
        number = input('Number: ')
        self.test_list['Number: '] = number
        number2 = input('Number2: ')
        self.test_list['Number2: '] = number2
        print(self.test_list)

        self.num_list = {name:self.test_list}
        #print(self.num_list)
        pass
    def main(self):
        self.import_contacts()
        while True:
            self.add_to_list()
            self.print()
            self.save_contacts()
    def print(self):
        for key, value in self.num_list.items():
            print(key, value)
            pass

    def save_contacts(self):
        with open('test_file.txt', 'a', encoding='utf-8') as file:
            for name, number in self.num_list.items():
                file.write(f'{name}; {number}\n')


    def import_contacts(self):
        with open('test_file.txt', 'r', encoding='utf-8') as file:
            file_string = file.readlines()
            for string in file_string:
                string = string.strip()
                name, number = string.split('; ')
                #print(type(name), type(number))
                number = eval(number)
                self.num_list = {name: number}


start = Test()
start.main()