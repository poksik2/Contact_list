import json
import os.path


# naming

class BookMessage:
    def get_menu_msg(self) -> str:
        return 'Что будем делать? (Посмотреть - 1, Добавить - 2, Удалить - 3, Редактировать - 4, Выход - Any Key): '

    def get_exit_msg(self) -> None:
        print('ВСЕГО ХОРОШЕГО!!!')


class Book:
    title = '====Список контактов===='
    NUMBER_LENGTH = 11

    # naming

    def __init__(self) -> None:
        # naming
        # порядок объявления и вызова функций
        self.list = []
        self.dict = {}
        self.msg_creator = BookMessage()

    def main(self) -> None:
        try:
            self.start_program()
        finally:
            self.complete()

    def start_program(self):
        self.check_file()
        while True:
            choice = self.create_choice()
            self.initialize_contacts()

            if choice == '1':
                self.reading()
            elif choice == '2':
                self.handle_add_choice()
            elif choice == '3':
                self.dellite()
            elif choice == '4':
                self.edit_number()
            else:
                self.complete()

    def initialize_contacts(self):
        # проверяет есть ли файл, если есть записывает из него контакты в contacts
        # или создает новый файл
        pass

    def create_choice(self) -> str:
        return input(self.msg_creator.get_menu_msg())

    def complete(self) -> None:
        self.get_exit_msg()
        exit()

    def writing(self) -> None:
        # naming
        name = str(input('Введите имя: '))
        self.validate_name(name)
        number = input('Введите номер: ')
        self.validate_number(number)
        self.dict[name] = number
        self.convert_dict_to_list()
        self.import_to_file(self.list)
        # Запись в dict, конвертация в list и запсь в файл

    def handle_add_choice(self) -> None:
        name = input('Введите имя: ')
        self.validate_name(name)
        phone_number = input('Введите номер: ')
        self.validate_number(phone_number)

        # добавить проверку номера на уникальность
        self.get_noadd_number(phone_number)
        self.add_contact(name, phone_number)

    def add_contact(self, name: str, phone_number: str) -> None:
        # добавить валидацию имени по уникальности и номера по формат
        self.contacts[name] = phone_number
        self.export_to_file()

    def reading(self) -> None:
        # читаем только из коллекции contacts
        self.print_title()
        self.exports_from_file()
        self.Empry_list()
        self.listing()
        # Печать заголовка, чтение из файла в list и конвертация в dict, Вывод в столбик

    def dellite(self) -> None:
        # удаляем только из коллекции contacts
        self.exports_from_file()
        self.dell()
        self.import_to_file(self.list)
        # Чтение из файла в list и конвертация в dict, удаление и конвертация в dict, запись в файл

    def exports_from_file(self) -> None:
        # naming
        exports = open('Contacts.txt', 'rb')
        self.list = exports.read()
        self.convert_list_to_dict()
        exports.close()
        # Открытие файла, чтение в list, конвертация в dict, закрытие файла

    def import_to_file(self, list) -> None:
        imports = open('Contacts.txt', 'wb')
        imports.write(list)
        imports.close()
        # Открытие файла, запись в файл, закрытие файла

    def dell(self) -> None:
        # объединить делиты
        name = str(input('Введите имя: '))
        del self.dict[name]
        print(f'Контакт {name} удален')
        self.convert_dict_to_list()
        # Удаление элемента в dict, конвертация в list

    def check_file(self) -> None:
        if os.path.exists("Contacts.txt"):
            return
        else:
            self.list.append(self.title)
            self.open_close()
        # Проверка наличия файла

    def print_title(self) -> None:
        print(self.title)
        # Печать заголовка

    def get_exit_msg(self) -> None:
        print('ВСЕГО ХОРОШЕГО!!!')

    def get_empty_list_msg(self) -> None:
        print('Список контактов пуст')

    def Empry_list(self) -> None:
        if self.list:
            for contact in self.list:
                continue
        else:
            self.get_empty_list_msg()
        # Проверка на пустоту файла

    def validate_name(self, name: str):
        # solid - почитай
        # s - single responsible principle (принцип единственной ответственности)
        if not name:
            self.handle_empty_name()
        elif name in self.dict:
            # пользак уже есть. хотите перезаписать?
            new_number = input('Введите новый номер : ')
            self.dict[name] = new_number
            self.convert_dict_to_list()
            self.import_to_file(self.list)
            return self.main()

        # Проверка на совпадение и пустоту имени

    def handle_empty_name(self):
        print('Имя не может быть пустым')
        self.writing()

    def validate_number(self, number):
        if len(number) == self.NUMBER_LENGTH:
            print('Контакт успешно добавлен')
            return
        else:
            # print('Не правильная длина номера')
            print(f'Длина номера должна быть равна {self.NUMBER_LENGTH}')
            self.main()
        # Проверка номера по формату

    def edit_number(self):
        self.exports_from_file()
        name = input('Введите имя: ')
        old_name = 1
        new_name = 'Введите новое имя или нажмите ENTER, чтобы оставить прежнее имя'
        new_name = new_name or old_name
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


my_list = Book()
my_list.main()
