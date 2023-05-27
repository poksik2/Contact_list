class BookMessage:
    MENU = 'Что будем делать? (Посмотреть - 1, Добавить или редактировать - 2, Удалить - 3,  Выход - Any Key): '
    TITLE = '====Список контактов===='
    SUCCESS_CREATED = 1
    # ПРОДОЛЖИ

    def get_menu_msg(self) -> str:
        return 'Что будем делать? (Посмотреть - 1, Добавить или редактировать - 2, Удалить - 3,  Выход - Any Key): '

    @staticmethod
    def tile_string() -> str:
        return '====Список контактов===='

    def enter_name_msg(self) -> str:
        return 'Введите имя контакта: '

    def enter_number_msg(self) -> str:
        return 'Ведите номер контакта: '

    def enter_new_name_msg(self):
        return 'Ведите новый номер контакта: '

    def number_len_err(self):
        return f'Длинна номера должна быть {BookList.NUMBER_LEN}'

    def empty_name_msg(self) -> str:
        return 'Имя не может быть пустым'

    def overwrite_name_or_no(self, name) -> str:
        # добавить новый или изменить старый
        return f'Контакт с таким именем уже есть. Хотите изменить номер для {name} (Да - 1, Нет - 2): '

    def get_exit_msg(self) -> str:
        return 'ВСЕГО ХОРОШЕГО!!!'

    def enter_name_for_dellete(self) -> str:
        return 'Введите имя контакта который хотите удалить: '

    def delete_contact_true(self) -> str:
        return 'Контакт удален!'

    def added_successfully_contact(self) -> str:
        return 'Контакт успешно добавлен!'

    def file_if_creating(self) -> str:
        # naming
        # file_was_created
        return 'Файл создан'


class BookList:
    # добавить эти функции
    # create_name
    # create_number
    # naming:
    # метод должен содержать глагол в начальной форме (create, read, write, validate)
    # и не быть слишком абстрактным (не содержать общие слова/фразы типа: информация,
    # данные, список, коллекция),а быть конкретным (контакты, фио)
    NUMBER_LEN = 5

    def __init__(self):
        # реализовать классы для чтения, добавления, удаления и тд контактов
        # self.creator = 1
        # self.reader|getter = 1
        self.contact_list = {}  # naming
        self.msg_creator = BookMessage()

    def main(self):
        try:
            self.start_program()
        finally:
            self.complete_program()

    def start_program(self):
        # пофиксить повторный вызов этого метода
        while True:
            self.initialize_contact()
            choice = self.suggest_are_choice()
            if choice == '1':
                self.read_the_list()
            elif choice == '2':
                self.write_contact()
            elif choice == '3':
                self.delete_contact()
            else:
                self.write_list_to_file()
                self.complite()

    def complete_program(self) -> None:
        print(self.msg_creator.get_exit_msg())
        exit()

    def initialize_contact(self):
        # !!!!
        try:
            self.import_to_list()
        except:
            self.create_file()

    def import_to_list(self):
        # название файла в переменную
        with open('my_contact_list.txt', 'r', encoding='utf-8') as file:
            file_string = file.readlines()
            for string in file_string:
                string = string.strip()
                name, number = string.split(', ')
                # write_contact
                self.contact_list[name] = number

    def create_file(self):
        with open('my_contact_list.txt', 'w', encoding='utf-8') as file:
            return print(self.msg_creator.file_if_creating)

    def suggest_are_choice(self) -> str:
        # naming
        # create_menu
        return input(self.msg_creator.get_menu_msg())

    def read_the_list(self):
        # naming
        print(self.msg_creator.tile_string())
        for key, value in self.contact_list.items():
            print(key, value)

    def write_contact(self):
        # naming
        self.receiving_and_verifying_and_write_data()

    def receiving_and_verifying_and_write_data(self):
        # naming
        name = input(self.msg_creator.enter_name_msg())
        self.validation_name(name)
        phone_number = input(self.msg_creator.enter_number_msg())
        self.validation_number(phone_number)
        self.write_data_to_list(name, phone_number)

    def entering_name(self):
        name = 'name'
        self.validation_name(name)
        return name

    def input_name(self):
        name = input(self.msg_creator.enter_name_msg())
        return name

    def validation_name(self, name: str):
        # naming
        if not name:
            self.action_empty_name()
        else:
            self.action_match_name(name)

    def action_empty_name(self):
        print(self.msg_creator.empty_name_msg())
        self.write_contact()

    def action_match_name(self, name):
        if name in self.contact_list:
            choice_action_name = input(self.msg_creator.overwrite_name_or_no(name))
            self.choice_action_for_repeat_name(choice_action_name, name)

    def choice_action_for_repeat_name(self, choice_action_name, name):
        if choice_action_name == '1':
            new_number = input(self.msg_creator.enter_new_name_msg())
            self.validation_number(new_number)
            # нужен метод для редактирования
            self.contact_list[name] = new_number
            self.write_list_to_file()  # !!!!
            self.start_program()  # !!!!

        elif choice_action_name == '2':
            self.write_contact()

    def entering_number(self):
        phone_number = self.input_phone_number()
        self.validation_number(phone_number)
        return phone_number

    def input_phone_number(self):
        phone_number = input(self.msg_creator.enter_number_msg())
        return phone_number

    def validation_number(self, number):
        if len(number) == self.NUMBER_LEN:
            print(self.msg_creator.added_successfully_contact())
        else:
            print(self.msg_creator.number_len_err())
            # запустить ввод номера повторно
            self.start_program()

    def write_data_to_list(self, name, phone_number):
        self.contact_list[name] = phone_number
        self.start_program()  # !!!!

    def delete_contact(self):
        name = self.input_name_for_delete()
        del self.contact_list[name]
        self.write_list_to_file()
        print(self.msg_creator.delete_contact_true())

    def input_name_for_delete(self):
        return input(self.msg_creator.enter_name_for_dellete())

    def write_list_to_file(self):
        with open('my_contact_list.txt', 'w', encoding='utf-8') as file:
            for name, number in self.contact_list.items():
                file.write(f'{name}, {number}\n')
                file.writelines(f'{name}, {number}')  # если работает это, то выбери его


start = BookList()
start.main()
