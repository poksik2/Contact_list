import json
import os.path

class book:
    title = '====Список контактов===='
    def __init__(self) -> None:
        self.list = []
        self.dict = {}

    def main(self):
        self.check_file()
        while True:
            try:    # Отлов KeyboardInterrupt
                choice = (input('Что будем делать? (Посмотреть - 1, Добавить - 2, Удалить - 3, Редактировать - 4, Выход - Any Key): '))
            except KeyboardInterrupt:
                self.get_exit_msg()
                break
            if choice == '1':
                self.reading()
            elif choice == '2':
                self.wtiting()
            elif choice == '3':
                self.dellite()
            elif choice == '4':
                self.edit_number()
            else:
                self.get_exit_msg()
                break

    def wtiting(self) -> None:
        name = str(input('Введите имя: '))
        self.validate_name(name)
        number = input('Введите номер: ')
        self.validate_number(number)
        self.dict[name] = number
        self.convert_dict_to_list()
        self.import_to_file(self.list)
        # Запись в dict, конвертация в list и запсь в файл

    def reading(self) -> None:
        self.print_title()
        self.exports_from_file()
        self.Empry_list()
        self.listing()
        # Печать заголовка, чтение из файла в list и конвертация в dict, Вывод в столбик

    def dellite(self):
        self.exports_from_file()
        self.dell()
        self.import_to_file(self.list)
        #Чтение из файла в list и конвертация в dict, удаление и конвертация в dict, запись в файл

    def exports_from_file(self):
        exports = open('Contacts.txt', 'rb')
        self.list = exports.read()
        self.convert_list_to_dict()
        exports.close()
        # Открытие файла, чтение в list, конвертация в dict, закрытие файла

    def convert_dict_to_list(self):
        self.list = json.dumps(self.dict, sort_keys=True)
        self.list = bytes(self.list, encoding='utf-8')

    def import_to_file(self, list):
        imports = open('Contacts.txt', 'wb')
        imports.write(list)
        imports.close()
        # Открытие файла, запись в файл, закрытие файла
    def convert_list_to_dict(self):
        self.list = bytes(self.list)
        self.dict = json.loads(self.list)

    def listing(self):
        for key, value in self.dict.items():
            print(key, ':', value)
        # Вывод dict построчно
    def dell(self):
        name = str(input('Введите имя: '))
        del self.dict[name]
        print(f'Контакт {name} удален')
        self.convert_dict_to_list()
        # Удаление элемента в dict, конвертация в list

    def check_file(self):
        if os.path.exists("Contacts.txt"):
            return
        else:
            self.list.append(self.title)
            self.open_close()
        # Проверка наличия файла

    def print_title(self):
        print(self.title)
        # Печать заголовка
    def open_close(self):
        self.convert_dict_to_list()
        self.import_to_file(self.list)
        self.convert_list_to_dict()
        self.exports_from_file()

    def get_exit_msg(self):
        print('ВСЕГО ХОРОШЕГО!!!')

    def get_empty_list_msg(self) -> None:
        print('Список контактов пуст')

    def Empry_list(self):
        if self.list:
            for contact in self.list:
               continue
        else:
            self.get_empty_list_msg()
        # Проверка на пустоту файла
    def validate_name(self, name:str):
        if name in self.dict:
            new_number = input('Введите новый номер : ')
            self.dict[name] = new_number
            self.convert_dict_to_list()
            self.import_to_file(self.list)
            return self.main()
        if name == '':
            print('Имя не может быть пустым')
            return self.main()
        # Проверка на совпадение и пустоту имени
    def validate_number(self, number):
        if len(number) == 11:
            print('Контакт успешно добавлен')
            return
        else:
            print('Не правильная длина номера')
            self.main()
        # Проверка номера по формату

    def edit_number(self):
        self.exports_from_file()
        name = input('Введите имя: ')
        if name in self.dict:
            new_number = input('Введите номер: ')
            self.dict[name] = new_number
            self.convert_dict_to_list()
            self.import_to_file(self.list)
            return
        else:
            print('Контакт с таким именем не найден!')
            return
        # Редактор номера



my_list = book()
my_list.main()
