def add_contact():
    name = input('Введите имя контакта: ')
    about = input('Введите описание контакта: ')
    number = input('Введите номер контакта: ')
    col = name + ', ' + about + ', ' + number + ';'
    return col


def add_contact_json():
    name = input('Введите имя контакта: ')
    about = input('Введите описание контакта: ')
    number = input('Введите номер контакта: ')
    contact = {name: [about, number]}
    return contact


def add_contact_csv():
    name = input('Введите имя контакта: ')
    about = input('Введите описание контакта: ')
    number = input('Введите номер контакта: ')
    contact = [name, about, number]
    return contact


def find_contact():
    name = input('Введите имя контакта: ')
    return name


def action():
    act = input('Введите действие: ')
    return act


def path_file():
    path = input('Введите путь: ')
    return path


def help():
    print('Это вторая версия телефонного справочника.')
    print('Справочник работает с ".txt" ".json" ".csv" форматами. Для работы укажите путь к файлу и выберете действие: \n \
"/r" - чтение \n \
"/w" - запись \n \
"/f" - поиск по справочнику \n \
"/d" - удаление из справочника \n \
"/add" - объединение телефонных книг (работает с файлами формата ".json"')


def format_file(path):
    path = path.split('.')
    if path[-1] == 'txt':
        return 'txt'
    elif path[-1] == 'json':
        return 'json'
    elif path[-1] == 'csv':
        return 'csv'
