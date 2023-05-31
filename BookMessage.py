class BookMessage:
    NUMBER_LEN = 5
    MENU = 'Что будем делать? (Посмотреть - 1, Добавить - 2, Удалить - 3,  Выход - Any Key): '
    TITLE = '====Список контактов===='
    ENTER_NAME = 'Введите имя контакта: '
    ENTER_NUMBER = 'Ведите номер контакта: '
    ERR_NUMBER_LEN = f'Длинна номера должна быть {NUMBER_LEN}'
    EMPTY_NAME = 'Имя не может быть пустым'
    OVERWRITE_NUMBER = 'Контакт с таким именем уже есть. Хотите создать новый или изменить существующий (Создать - 1, Редактировать - 2): '
    EXIT = '\nВСЕГО ХОРОШЕГО!!!'
    DELETE_CONTACT = 'Контакт удален!'
    SUCCESS_ADD = 'Контакт успешно добавлен!'
    SUCCESS_CREATED = 'Файл создан'
    # ПРОДОЛЖИ

    #def get_menu_msg(self) -> str:
        #return 'Что будем делать? (Посмотреть - 1, Добавить или редактировать - 2, Удалить - 3,  Выход - Any Key): '
    #def tile_string() -> str:
        #return '====Список контактов===='
    #def enter_name_msg(self) -> str:
        #return 'Введите имя контакта: '
    #def enter_number_msg(self) -> str:
        #return 'Ведите номер контакта: '
   # def enter_new_name_msg(self):
        #return 'Ведите новый номер контакта: '
    #def number_len_err(self):
        #return f'Длинна номера должна быть {BookList.NUMBER_LEN}'
    #def empty_name_msg(self) -> str:
        #return 'Имя не может быть пустым'
    #def overwrite_name_or_no(self, name) -> str:
        # добавить новый или изменить старый
        #return f'Контакт с таким именем уже есть. Хотите изменить номер для {name} (Да - 1, Нет - 2): '
    #def get_exit_msg(self) -> str:
        #return 'ВСЕГО ХОРОШЕГО!!!'

    #def enter_name_for_dellete(self) -> str:
        #return 'Введите имя контакта который хотите удалить: '

    #def delete_contact_true(self) -> str:
        #return 'Контакт удален!'

    #def added_successfully_contact(self) -> str:
        #return 'Контакт успешно добавлен!'

    #def file_if_creating(self) -> str:
        # naming
        # file_was_created
        #return 'Файл создан'