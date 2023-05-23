# -*- coding: utf-8 -*-
# !/usr/bin/env python
import pickle


class ContactList:
    # реализовать сохранение и чтение в файл
    CONTACTS_FILE_NAME = 'book.txt'

    def __init__(self):
        self.contacts = {}

    def initialize_contacts(self):
        # проверить есть ли файл с контактами, если нет, то создать
        # если есть, то занести в коллекцию self.contacts
        # реализуй две вариации запись после каждого добавления/удаления или только по завершению программы
        # try/except/finally - на случай внештатного завершения программы
        pass

    def main(self) -> None:
        while True:
            # добавить редактирование
            choice = (input('Что будем делать? (Посмотреть - 1, Добавить - 2, Удалить - 3, Выйти - 4): '))  # вынеси в метод

            if choice == '1':
                self.get_all_contacts_choice()
            elif choice == '2':
                self.add_contact_choice()
            elif choice == '3':
                self.delete_contact_choice()
            else:
                self.get_exit_msg()
                break
            print()

    def get_all_contacts_choice(self) -> None:
        # при первом запросе брать контакты из файла, далее из коллекции self.contacts
        self.import_from_file()
        self.get_contact_list_title()
        self.get_all_contacts()

    def get_all_contacts(self) -> None:
        # выводить контакты отсортированные по имени
        self.get_all_contacts_sort()
        if self.contacts:
            # отсортировать и вывести после if
            for contact in self.contacts:
                print(contact, self.contacts[contact])
        else:
            self.get_empty_list_msg()

    def get_all_contacts_sort(self) -> None:
        # нейминг
        self.contacts = dict(sorted(self.contacts.items()))

    def get_contact_list_title(self) -> None:
        print('****СПИСОК КОНТАКТОВ****')

    def get_empty_list_msg(self) -> None:
        print('Список контактов пуст')

    def import_from_file(self):
        # через read() or readlines()
        with open(self.CONTACTS_FILE_NAME, 'rb') as a:
            self.contacts = pickle.load(a)

    def add_contact_choice(self) -> None:
        name = input('Введите имя: ')
        phone_number = input('Введите номер: ')

        self.validation_name(name)
        # добавить проверку номера на уникальность
        self.get_noadd_number(phone_number)
        self.add_contact(name, phone_number)

    def add_contact(self, name: str, phone_number: str) -> None:
        # добавить валидацию имени по уникальности и номера по формат
        self.contacts[name] = phone_number
        self.export_to_file()

    def validation_name(self, name: str) -> None:
        # должен быть глагол validate
        # проверка на ненулевость имени

        # предложить перезаписать чела, если имя уже существует
        if name in self.contacts:
            self.get_noadd_msg(name)
            self.main()  # main внутри функций не вызывать
        else:
            self.get_add_msg(name)

    def get_add_msg(self, name: str) -> None:
        print(f'Контакт "{name}" успешно добавлен')

    def get_noadd_msg(self, name: str) -> None:

        print(f'Контакт "{name}" уже добавлен')

    def get_noadd_number(self, phone_number: str):
        # get_already_exit_msg
        if len(phone_number) != 5:
            print('Некорректно введен номер')
            self.main()  # main внутри функций не вызывать

    def delete_contact_choice(self) -> None:
        name = input('Введите имя: ')
        self.delete_contact(name)
        self.get_delete_msg(name)

    def delete_contact(self, name: str) -> None:
        # обработать удаление не существующего контакта !!!!
        self.import_from_file()
        self.contacts.pop(name)
        self.export_to_file()

    def get_delete_msg(self, name: str) -> None:
        print(f'Контакт "{name}" успешно удален')

    def get_exit_msg(self):
        print('ВСЕГО ХОРОШЕГО!!!')

    def export_to_file(self):
        # попробуй через write
        with open('book.txt', "wb") as a:
            pickle.dump(self.contacts, a)


my_contacts = ContactList()
my_contacts.main()

# хранить контакты в таком формате
# имя номер
# имя, номер
# имя, номер
# имя, номер
# имя, номер
# имя, номер
# имя, номер
# имя, номер
