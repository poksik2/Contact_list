filename = 'my_contacts.txt'


def write_dict_elements_to_file():
    contacts = {
        'a': 1,
        'b': 2,
    }

    with open('my_contacts.txt', 'w', encoding='utf-8') as file:
        for name, number in contacts.items():
            file.write(f'{name}, {number}\n')


def read_or_create_file():
    try:
        with open('my_contacts.txt', 'r', encoding='utf-8') as file:
            file_strings = file.readlines()
            for string in file_strings:
                string = string.strip()
                name, number = string.split(', ')
    except:
        with open('my_contacts.txt', 'w', encoding='utf-8') as file:
            read_or_create_file()


read_or_create_file()
# write_dict_elements_to_file()
